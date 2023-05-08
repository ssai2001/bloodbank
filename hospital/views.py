from django.shortcuts import render,redirect
from django.http import JsonResponse

from .models import BloodBank,BloodOrder


# Create your views here.


def index(request):
    if request.session.get('orders'):
        del request.session['orders']
    lat = request.user.latitude
    # print(lat)
    lng = request.user.longitude
    # print(lng)
    un_blood_bank = []
    length = []
    i=0
    bloodbanks = BloodBank.objects.all()
    for b in bloodbanks:
        dist = {}
        i=i+1
        length.append(i)
        dist['id'] = b.id
        dist['blood_bank_name'] = b.blood_bank_name
        distance = (((b.latitude-lat)**2) + ((b.longitude-lng)**2))
        dist['distance'] = distance
        dist['address'] = b.address
        un_blood_bank.append(dist)
    # print(un_blood_bank)
    o_blood_bank = (sorted(un_blood_bank,key=lambda x:x['distance']))
    # print(o_blood_bank)
    
    context = {
        'nearest':o_blood_bank,
        'length':length
    }
    return render(request,'hospital/index.html',context)

def menu(request, bb_id):
    global id 
    id = bb_id
    blood = BloodBank.objects.get(id = bb_id)
    context = {
        'blood':blood,
    }
    # print(blood)
    return render(request,'hospital/menu.html',context)

def addToCart(request):
    if request.method == "POST":
        print(id)
        b_group = request.POST.get('b_group')
        quantity = request.POST.get('quantity')
        order = {}
        if request.session.get('orders'):
            order = request.session.get('orders')
        order[b_group] = quantity
        request.session["orders"] = order
        print(order)
        return redirect('hospital_menu',id)

        
def cart(request):
    orders = request.session.get('orders')
    items = []
    total_quantity=0
    if orders:
        for b_group,quantity in orders.items():
            items.append({
                'b_group':b_group,
                'quantity':quantity,
            })
            total_quantity+=int(quantity)
    print(items)
    context={
        'items':items,
        'total_quantity':total_quantity
    }
    return render(request,'hospital/cart.html',context)

def delete(request, b_group):
    orders = request.session.get('orders')
    del orders[b_group]
    request.session['orders'] = orders
    return redirect('hospital_cart')

def placeOrder(request):
    orders = request.session.get('orders')
    blood_list = {
        'O+ve':0,
        'O-ve':0,
        'A+ve':0,
        'A-ve':0,
        'B+ve':0,
        'B-ve':0,
        'AB+ve':0,
        'AB-ve':0,
    }
    if orders:
        order_details=""
        total_quantity=0
        for b_group,quantity in orders.items():
            blood_list[b_group] = int(quantity)
            total_quantity += int(quantity)
            order_details += f"{b_group}x{quantity},"
        print(blood_list)
        try:
            b_bank = BloodBank.objects.get(id=id)
            print(b_bank.id)
            print(request.user.id)
            order = BloodOrder.objects.create(
                user = request.user,
                sourceLatitude = b_bank.latitude,
                sourceLongitude = b_bank.longitude,
                destinationLatitude = request.user.latitude,
                destinationLongitude = request.user.longitude,
                orderDetails = order_details,
                totalQuantity = total_quantity
            )
            order.save()
        except Exception as e:
            print(e)
        try:
            blood = BloodBank.objects.get(id = id)
            blood.o_pos_group -= int(blood_list['O+ve'])
            blood.o_neg_group -= int(blood_list['O-ve'])
            blood.a_pos_group -= int(blood_list['A+ve'])
            blood.a_neg_group -= int(blood_list['A-ve'])
            blood.b_pos_group -= int(blood_list['B+ve'])
            blood.b_neg_group -= int(blood_list['B-ve'])
            blood.ab_pos_group -= int(blood_list['AB+ve'])
            blood.ab_neg_group -= int(blood_list['AB-ve'])
            blood.save()
        except Exception as e:
            print(e)
        del request.session['orders']
    return redirect('hospital_order_history')

def trackOrder(request):
    try:
        points = BloodOrder.objects.get(is_delivered=False,user_id=request.user.id)
        context = {
            'is_delivered':points.is_delivered
        }
        return render(request,'hospital/trackOrder.html',context)
    except Exception as e:
        print(e)
    context={
        'is_delivered':True
    }
    return render(request,'hospital/trackOrder.html',context)
    

def orderHistory(request):
    orders = BloodOrder.objects.filter(user=request.user).order_by('-id')
    list = []
    total = []
    for o in orders:
        od = o.orderDetails
        so = od.split(',')
        # print(so)
        items = []
        i=0
        total_quantity=0
        for x,i in zip(so,range(len(so)-1)):
            i=i+1
            str = x.split('x')
            # print(str)
            b_group = str[0]
            quantity = str[1]
            total_quantity += int(quantity)
            # print(total_price)
            items.append({
                'b_group':b_group,
                'quantity':quantity,
            })
        total.append({
            'id':o.id,
            'delivered':o.is_delivered,
            'created':o.created_at,
            'total_quantity':total_quantity,
        })
        list.append(items)
    # print(total)
    # print(list)
    context={
        'list':list,
        'total':total
    }
    return render(request,'hospital/orderHistory.html',context)


# Track Order
def my_ajax_view(request):
    try:
        coordinates = BloodOrder.objects.get(is_delivered=False,user_id=request.user.id)
        print(coordinates)
    except Exception as e:
        print(e)
    points = {
        'source_latitude':coordinates.sourceLatitude,
        'source_longitude':coordinates.sourceLongitude,
        'destination_latitude':coordinates.destinationLatitude,
        'destination_longitude':coordinates.destinationLongitude
    }
    print(points)
    data = {
        'coordinates': points
    }
    return JsonResponse(data)