from django.shortcuts import render
from Rent.models import *
from Rent.forms import *
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login


def user_client(user,client):
    if(client):
        try:
            Client.objects.get(user=user)
            return False
        except Exception as e:
            return True
    else:
        try:
            Client.objects.get(user=user)
            return True
        except Exception as e:
            return False

def user_executive(user,executive):
    if(executive):
        try:
            Executive.objects.get(user=user)
            return False
        except Exception as e:
            return True
    else:
        try:
            Executive.objects.get(user=user)
            return True
        except Exception as e:
            return False
        

