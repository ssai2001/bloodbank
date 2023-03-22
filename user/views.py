from django.shortcuts import redirect, render
from .models import customUser
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def donor_signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get("next"))
            return redirect('doner_home')
        else:
            messages.error(request, "Invalid credentials")
    return render(request,'user/donor-signin.html')

def hospital_signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get("next"))
            return redirect('hospital_home')
        else:
            messages.error(request, "Invalid credentials")
    return render(request,'user/hospital-signin.html')

def donor_signup(request):
    if request.method == "POST":
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        bloodgroup = request.POST.get('bloodgroup')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        contact = request.POST.get('contact')

        error = False

        print(f_name, l_name, username, email, password, bloodgroup, contact)

        if customUser.objects.filter(username=username).exists():
            # print('SIC already taken')
            messages.error(request,"Username already exists")
            error = True
        
        if customUser.objects.filter(email=email).exists():
            messages.error(request,"E-mail already exists")
            error = True
        
        if(error):
            return render(request,'donor/signup.html')

        try:
            user = customUser.objects.create_user(
                first_name = f_name,
                last_name = l_name,
                b_group = bloodgroup,
                username = username,
                email = email,
                password = password,
                contact = contact
            )
            user.save()
            # print('user created')
            messages.success(request,'Account created successfully. Login to continue')
            return redirect('donor_signin')
        except Exception as e:
            print(e)
    return render(request,'user/donor-signup.html')

def hospital_signup(request):
    if request.method == "POST":
        h_name = request.POST.get('hospital_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        contact = request.POST.get('contact')

        error = False

        print(h_name, username, email, password)

        if customUser.objects.filter(username=username).exists():
            # print('SIC already taken')
            messages.error(request,"SIC already exists")
            error = True
        
        if customUser.objects.filter(email=email).exists():
            messages.error(request,"E-mail already exists")
            error = True
        
        if(error):
            return render(request,'user/hospital-signup.html')

        try:
            user = customUser.objects.create_user(
                first_name = h_name,
                last_name = 'hospital',
                username = username,
                email = email,
                password = password,
                contact = contact,
                is_staff = True
            )
            user.save()
            # print('user created')
            messages.success(request,'Account created successfully. Login to continue')
            return redirect('hospital_signin')
        except Exception as e:
            print(e)
    return render(request,'user/hospital-signup.html')

def log_out(request):
    logout(request)
    return redirect('index')