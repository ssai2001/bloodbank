from django.shortcuts import render,redirect
from .models import BloodDepot,Order

# Create your views here.

def index(request):
    return render(request,'hospital/index.html')

def menu(request):
    blood = BloodDepot.objects.all()
    context = {
        'blood':blood,
    }
    return render(request,'hospital/menu.html',context)

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
            order_details += f"{b_group}x{quantity},"
        try:
            order = Order.objects.create(
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
    orders = Order.objects.filter(user=request.user).order_by('-id')
    list = []
    total = []
    for o in orders:
        od = o.orderDetails
        so = od.split(',')
        # print(so)
        items = []
        i=0
        total_price=0
        for x,i in zip(so,range(len(so)-1)):
            i=i+1
            str = x.split('x')
            # print(str)
            b_group = str[0]
            quantity = str[1]
            b_type = BloodDepot.objects.get(b_group=b_group)
            price = int(quantity) * int(b_type.price)
            total_price += price
            # print(total_price)
            items.append({
                'b_group':b_group,
                'quantity':quantity,
                'price':price,
            })
        total.append({
            'id':o.id,
            'delivered':o.is_delivered,
            'created':o.created_at,
            'total_price':total_price,
        })
        list.append(items)
    # print(total)
    # print(list)
    context={
        'list':list,
        'total':total
    }
    return render(request,'hospital/orderHistory.html',context)
