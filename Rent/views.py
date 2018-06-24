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
        

def index(request):
    data = {}
    data['name'] = 'Car'
    data["request"] = request
    
    try:
        cliente = Client.objects.get(user=request.user)
        object_list = Car.objects().order_by('-id')

        paginator = Paginator(object_list, 10)
        page = request.GET.get('page')

        try:
            data['object_list'] = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            data['object_list'] = paginator.page(1)
        except EmptyPage:
            data['object_list'] = paginator.page(paginator.num_pages)
            
        template_name = 'index.html'
        return render(request, template_name, data)
        
    except Exception as e:                       
        template_name = 'index.html'
        return render(request, template_name, data)
    
@login_required(login_url='/auth/login')    
def list_cars(request):
    #si es false el super admin no podra entrar
    if(user_client(request.user,False) and user_executive(request.user,False)):
        return redirect('index')
    data= {}
    data["request"] = request
    object_list = Car.objects.all().order_by('-id')

    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)
    template_name = 'list_cars.html'
    return render(request, template_name, data)
    
def car_add(request):
    data = {}
    data["request"] = request
    if request.method == "POST":
        data['form'] = CarForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('list_cars')

    else:
        data['form'] = CarForm()

    template_name = 'add_car.html'
    return render(request, template_name, data)

def delete_car(request, id):
    data = {}
    template_name = 'list_cars.html'
    data['car'] = Car.objects.all()
    Car.objects.filter(pk=id).delete()
    return HttpResponseRedirect(reverse('list_cars'))

def edit_car(request, car_id):
    data = {}
    data['tittle'] = "Editar auto"
    data["request"] = request
    if request.POST:
        formCar = EditCar(request.POST, request.FILES, instance=Car.objects.get(pk=car_id))
        if formCar.is_valid():
            formCar.save()
            return redirect('list_cars')
    template_name = 'edit.html'
    data['data'] = EditCar(instance=Car.objects.get(pk=car_id))

    return render(request, template_name, data)
