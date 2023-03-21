from django.shortcuts import render
from donationcamp.models import organizerDetails,donerDetails

# Create your views here.

def index(request):
    organizer = organizerDetails.objects.all()
    context = {
        'events':organizer,
    }
    return render(request,'doner/index.html',context)

def coupons(request):
    return render(request,'doner/coupons.html')

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
        'camps':organizers,
    }
    return render(request,'doner/participation.html',context)