from django.shortcuts import render,redirect
from donationcamp.models import organizerDetails,donerDetails
from . models import Coupons

import openpyxl

# Create your views here.

def index(request):
    organizer = organizerDetails.objects.all()
    context = {
        'events':organizer,
    }
    return render(request,'doner/index.html',context)

def delete(request):
    cpn = Coupons.objects.get(id=3)
    cpn.delete()
    return redirect('index')

def coupons(request):
    coupons = Coupons.objects.filter(user=request.user)
    context = {
        'coupons':coupons
    }
    return render(request,'doner/coupons.html',context)

def participation(request, user_email):
    donations = donerDetails.objects.filter(email = user_email)
    # print(donations)
    organizers = []
    for d in donations:
        # print(type(d.organizerId),d.organizerId.organizationName)
        organizer = organizerDetails.objects.get(id = d.organizerId.id)
        organizers.append(organizer)
    # for o in organizers:
    #     print(o.organizationName,o.date)
    context = {
        'range':range(1,len(organizers)+1),
        'camps':organizers,
    }
    return render(request,'doner/participation.html',context)