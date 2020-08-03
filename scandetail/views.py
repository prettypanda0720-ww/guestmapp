from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, JsonResponse
from order.models import Order
from django.contrib.auth.models import User
from account.models import Profile
import json

