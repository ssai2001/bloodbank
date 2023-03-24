from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from . models import organizerDetails,donerDetails
from doner.models import Coupons
from user.models import customUser
from random import randint
import openpyxl

# Create your views here.

def organize(request):
    if request.method == "POST":
        orgname = request.POST.get('organizationName')
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        date = request.POST.get('date')
        description = request.POST.get('shortDescription')
        password = randint(111111,999999)
        # coupons = 
        
        print(orgname,fullname,email,date,description)
        
        try:
            org_details = organizerDetails.objects.create(
                organizationName = orgname,
                organizerName = fullname,
                email = email,
                date = date,
                description = description,
                password = password
            )
            org_details.save()
            messages.success(request,'Registration successful.')
            send_mail(
                "Password for BloodBank",
                f"Your Password to start the Blood-Donation Camp is {password}",
                "psaimohancs@gmail.com",
                [email,],
                fail_silently=False
            )
            return redirect('organize')
        except Exception as e:
            print(e)
    return render(request,'camp/organize.html')

def delete_entry(request):
    entry = organizerDetails.objects.filter(organizerName="Pranjal Agrawal")
    entry.delete()
    return render(request,'camp/organize.html')

def verifyCamp(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            USER = {}
            user = organizerDetails.objects.get(email=email)
            USER['email'] = user.email
            if user.password == int(password):
                request.session["USER"] = USER
                print(request.session["USER"])
                messages.success(request,'Holaaaa Enjoy!!!')
                return redirect('startCamp')
            messages.error(request,'Invalid Credentials.')
        except Exception as e:
            messages.error(request,'No such Organizer is Present.')
            print(e)
    return render(request,'camp/organize.html')

def startCamp(request):
    global condition
    USER = request.session.get("USER")
    user = organizerDetails.objects.get(email=USER['email'])
    doners = donerDetails.objects.filter(organizerId=user.id)
    context = {
        'user':user,
        'doners':doners,
        'range':range(1,len(doners)+1),
    }
    return render(request,'camp/startCamp.html',context)

def donate(request):
    if request.method == "POST":
        organizerId = request.POST.get('organizerId')
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        bloodgroup = request.POST.get('bloodgroup')
        contact = request.POST.get('contact')
        # print(organizerId,fullname,email,bloodgroup,contact)
        try:
            doner = donerDetails.objects.create(
                organizerId = organizerDetails(organizerId),
                name = fullname,
                email = email,
                b_group = bloodgroup,
                contact = contact
            )
            doner.save()
        except Exception as e:
            print(e)
        # Alloting Coupons to first 3 users only.
        USER = request.session.get("USER")
        user = organizerDetails.objects.get(email=USER['email'])
        doners = donerDetails.objects.filter(organizerId=user.id)
        if len(doners) < 4:
            try:
                doner = customUser.objects.get(email=email)
                workbook = openpyxl.load_workbook('static/export1.xlsx')
                sheet = workbook.active
                cell_object = sheet.cell(row=1,column=1)
                print(cell_object.value)
                sheet.delete_rows(idx=1)
                workbook.save('static/export1.xlsx')
                try:
                    coupon = Coupons.objects.create(
                        user = customUser(doner.id),
                        couponCode = cell_object.value
                    )
                    coupon.save()
                except Exception as e:
                    print(e)
            except Exception as t:
                print(t)
    return redirect('startCamp')
    
