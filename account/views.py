from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, JsonResponse
from order.models import Order
from django.contrib.auth.models import User
from account.models import Profile
import json

def ajax_login(request):
    if request.method == 'POST':
        username = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    try:
                        order = Order.objects.get(userId = request.user)
                    except Order.DoesNotExist:
                        order = None
                    
                    if order is not None:
                        exist_order = True
                    else:
                        exist_order = False

                    data = {'success': True, 'order':exist_order}
                else:
                    data = {'success': False, 'message': 'User is not active'}
            else:
                data = {'success': False, 'message': 'Invalid username or password'}

    return JsonResponse(data)

def ajax_register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        email = request.POST.get('email', '').strip()

        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                data = {'success': False, 'message': 'User already exists.'}
            else:
                try:
                    user = User.objects.create_user(username, email, password)
                    Profile.objects.create(user = user, isFirstUser = True, name = username)
                    user = authenticate(username=username, password=password)
                    auth_login(request, user)
                    
                except:
                    data = {'success': False, 'message': 'Unexpected error occured.'}
                
                data = {'success': True, 'message': 'User create successfully'}

    return JsonResponse(data)

def ajax_logout(request):
    logout(request)

    return redirect('home')

def home(request):
    order = None
    if request.user.is_authenticated:
        try:
            order = Order.objects.get(userId = request.user)
        except Order.DoesNotExist:
            order = None

    return render(request, 'home.html', {'order':order})

@login_required
def guestmapp(request):
    return render(request, 'guestmapp.html')

@login_required
def planprices(request):
    # print(request.user.is_authenticated)
    return render(request, 'planprices.html')

@login_required
def ownguestmapp(request):
    return render(request, 'ownguestmapp.html')

@login_required
def newpassword(request):
    return render(request, 'newpassword.html')


