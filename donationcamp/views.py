from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from . models import organizerDetails,donerDetails
from random import randint

# Create your views here.

def organize(request):
    if request.method == "POST":
        orgname = request.POST.get('organizationName')
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        date = request.POST.get('date')
        description = request.POST.get('shortDescription')
        password = randint(111111,999999)
        
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
    entry = organizerDetails.objects.get(organizerName="Sital")
    entry.delete()
    return render(request,'camp/organize.html')

def startCamp(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = organizerDetails.objects.get(email=email)
            if user.password == int(password):
                messages.success(request,'Holaaaa Enjoy!!!')
                context = {
                    'user':user
                }
                return render(request,'camp/startCamp.html',context)
        except Exception as e:
            messages.error(request,'No such Organizer is Present.')
            print(e)
    return render(request,'camp/organize.html')

# def donate(request):
