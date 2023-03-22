from django.shortcuts import render,redirect
from .models import BloodAvailability

# Create your views here.

def index(request):
    blood = BloodAvailability.objects.all()
    context = {
        'blood':blood,
    }
    return render(request,'hospital/index.html',context)

def addToCart(request):
    if request.method == "POST":
        b_group = request.POST.get('b_group')
        quantity = request.POST.get('quantity')
        order = {}
        if request.session.get('orders'):
            order = request.session.get('orders')
        order[b_group] = quantity
        request.session["orders"] = order
        print(order)
        return redirect('hospital_home')

        
def cart(request):
    return render(request,'hospital/cart.html')

def trackOrder(request):
    return render(request,'hospital/trackOrder.html')

def orderHistory(request):
    return render(request,'hospital/orderHistory.html')
