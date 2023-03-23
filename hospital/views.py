from django.shortcuts import render,redirect
from .models import BloodDepot,Orders

# Create your views here.

def index(request):
    blood = BloodDepot.objects.all()
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
    orders = request.session.get('orders')
    items = []
    total_price=0
    if orders:
        for b_group,quantity in orders.items():
            b_type = BloodDepot.objects.get(b_group=b_group)
            price = int(quantity) * int(b_type.price)
            total_price += price
            items.append({
                'b_group':b_group,
                'quantity':quantity,
                'price':price
            })
    print(items)
    context={
        'items':items,
        'total_price':total_price
    }
    return render(request,'hospital/cart.html',context)

def delete(request, b_group):
    orders = request.session.get('orders')
    del orders[b_group]
    request.session['orders'] = orders
    return redirect('hospital_cart')

def placeOrder(request):
    orders = request.session.get('orders')
    if orders:
        order_details=""
        total_price=0
        for b_group,quantity in orders.items():
            b_type = BloodDepot.objects.get(b_group=b_group)
            price = int(quantity) * int(b_type.price)
            total_price += price
            order_details += f"{b_group} x {quantity}"
        try:
            order = Orders.objects.create(
                user = request.user,
                orderDetails = order_details,
                totalPrice = total_price
            )
            order.save()
        except Exception as e:
            print(e)
        del request.session['orders']
    return redirect('hospital_order_history')


def trackOrder(request):
    return render(request,'hospital/trackOrder.html')

def orderHistory(request):
    return render(request,'hospital/orderHistory.html')
