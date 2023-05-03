from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from hospital.models import BloodOrder

# Create your views here.

def index(request):
    return render(request,'pages/index.html')

def navigation(request,track_id):
    try:
        points = BloodOrder.objects.get(id=track_id)
        context={
            'latitude':points.destinationLatitude,
            'longitude':points.destinationLongitude,
            'track_id':track_id
        }
    except Exception as e:
        print(e)
    return render(request,'pages/navigationPage.html',context)

@csrf_exempt
def my_ajax_insert(request):
    if request.method == "POST":
        latitude = request.POST.get("lat")
        longitude = request.POST.get("long")
        user_id = request.POST.get("user_id")
        print(latitude)
        print(longitude)
        print(user_id)
        try:
            coordinates = BloodOrder.objects.get(id=user_id)
            coordinates.sourceLatitude = latitude
            coordinates.sourceLongitude = longitude
            coordinates.save()
        except Exception as e:
            print(e)
        return JsonResponse({"status": "success"})
    else:
        return JsonResponse({"status": "error","message":"Invalid Request Method"})