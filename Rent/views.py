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
    data['inicio'] = 0
    if (user_client(request.user,False)):
        data['inicio']= 1
    elif (user_executive(request.user,False)):
        data['inicio']= 2
    elif (request.user.is_staff == True):
        data['inicio'] = 3
    
    data['name'] = 'Car'
    data["request"] = request
    
    try:
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
            
        template_name = 'index.html'
        return render(request, template_name, data)
        
    except Exception as e:                       
        template_name = 'index.html'
        return render(request, template_name, data)


#Views Cars
@login_required(login_url='/auth/login')
def list_cars(request):
    
    data= {}
    data['inicio'] = 0
    if (user_client(request.user,False)):
        data['inicio']= 1
        # arreglar filter de autos del cliente
    elif (user_executive(request.user,False)):
        data['inicio']= 2
    elif (request.user.is_staff == True):
        data['inicio'] = 3
    
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

@login_required(login_url='/auth/login')
def car_add(request):
    #si es false el super admin no podra entrar
    if(user_client(request.user,False)):
        return redirect('cars')
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

@login_required(login_url='/auth/login')
def delete_car(request, id):
    #si es false el super admin no podra entrar
    if(user_client(request.user,False)):
        return redirect('cars')
    data = {}
    template_name = 'list_cars.html'
    data['car'] = Car.objects.all()
    Car.objects.filter(pk=id).delete()
    return HttpResponseRedirect(reverse('list_cars'))

@login_required(login_url='/auth/login')
def edit_car(request, car_id):
    #si es false el super admin no podra entrar
    if(user_client(request.user,False)):
        return redirect('cars')
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


#Views Ejecutives
@login_required(login_url='/auth/login')
def list_executives(request):
    #si es false el super admin no podra entrar
    data = {}
    data['inicio'] = 0
    
    if(user_client(request.user,False) or user_executive(request.user,False)):
        return redirect('cars')

    elif (request.user.is_staff == True):
        data['inicio'] = 3
        
    data["request"] = request
    object_list = Executive.objects.all().order_by('-id')

    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)
    template_name = 'list_executives.html'
    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def executive_add(request):
    #si es false el super admin no podra entrar
    if(user_client(request.user,False) or user_executive(request.user,False)):
        return redirect('cars')
    data = {}
    data['tittle'] = "Agregar Ejecutivo"
    data["request"] = request
    if request.method == "POST":
        print(request.POST)
        data['form'] = ExecutiveForm(request.POST, request.FILES)
        data['form2'] = UserForm(request.POST, request.FILES)

        if data['form2'].is_valid():
            # aca el formulario valido
            if data['form'].is_valid():
                sav = data['form'].save(commit=False)
                sav2 = User.objects.create_user(username= request.POST['username'], password= request.POST['password1'])
                sav.user = sav2
                sav.save()
            return redirect('list_executives')

    else:
        data['form2'] = UserForm()
        data['form'] = ExecutiveForm()

    template_name = 'add_executive.html'
    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def delete_executive(request, exe_id):
    #si es false el super admin no podra entrar
    if(user_client(request.user,False) or user_executive(request.user,False)):
        return redirect('cars')
    #si es false el super admin no podra entrar
    data = {}
    template_name = 'list_executives.html'
    data['executive'] = Executive.objects.all()

    ejecutivo = Executive.objects.get(pk=exe_id)
    usuario = User.objects.get(username = ejecutivo.user)
    User.objects.filter(username=ejecutivo.user).delete()

    return HttpResponseRedirect(reverse('list_executives'))

@login_required(login_url='/auth/login')
def edit_executive(request, exe_id):
    #si es false el super admin no podra entrar
    if(user_client(request.user,False) or user_executive(request.user,False)):
        return redirect('cars')
    data = {}
    data['tittle'] = "Editar Ejecutivo"
    data["request"] = request
    if request.POST:
        formExe = EditExecutive(request.POST, request.FILES, instance=Executive.objects.get(pk=exe_id))
        if formExe.is_valid():
            formExe.save()
            return redirect('list_executives')
    template_name = 'edit.html'
    data['data'] = EditExecutive(instance=Executive.objects.get(pk=exe_id))

    return render(request, template_name, data)

#Views Client
@login_required(login_url='/auth/login')
def list_clients(request):
    #si es false el super admin no podra entrar
    data = {}
    data['inicio'] = 0
    if (user_client(request.user,False)):
        return redirect('cars')
    elif (user_executive(request.user,False)):
        data['inicio']= 2
    elif (request.user.is_staff == True):
        data['inicio'] = 3
        
    data["request"] = request
    object_list = Client.objects.all().order_by('-id')

    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)
    template_name = 'list_clients.html'
    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def client_add(request):
    #si es false el super admin no podra entrar
    if(user_client(request.user,False)):
        return redirect('cars')
    data = {}
    data['title'] = "Agregar Cliente"
    data["request"] = request
    if request.method == "POST":
        print(request.POST)
        data['form'] = ClientForm(request.POST, request.FILES)
        data['form2'] = UserForm(request.POST, request.FILES)

        if data['form2'].is_valid():
            # aca el formulario valido
            if data['form'].is_valid():
                sav = data['form'].save(commit=False)
                sav2 = User.objects.create_user(username= request.POST['username'], password= request.POST['password1'])
                sav.user = sav2
                sav.save()
            return redirect('list_clients')
    else:
        data['form2'] = UserForm()
        data['form'] = ClientForm()

    template_name = 'add_client.html'
    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def delete_client(request,client_id):
    #si es false el super admin no podra entrar
    if(user_client(request.user,False)):
        return redirect('cars')
    data = {}
    template_name = 'list_clients.html'
    data['client'] = Client.objects.all()

    cliente = Client.objects.get(pk=client_id)
    usuario = User.objects.get(username = cliente.user)
    User.objects.filter(username=cliente.user).delete()
    print(usuario)
    print(usuario.username)

    return HttpResponseRedirect(reverse('list_clients'))



@login_required(login_url='/auth/login')
def edit_client(request, cli_id):
    #si es false el super admin no podra entrar
    if(user_client(request.user,False)):
        return redirect('cars')
    data = {}
    data['tittle'] = "Editar Cliente"
    data["request"] = request
    if request.POST:
        formCli = EditClient(request.POST, request.FILES, instance=Client.objects.get(pk=cli_id))
        if formCli.is_valid():
            formCli.save()
            return redirect('list_clients')
    template_name = 'edit.html'
    data['data'] = EditClient(instance=Client.objects.get(pk=cli_id))

    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def list_rents(request):
    #si es false el super admin no podra entrar
    data = {}
    data['inicio'] = 0
    if (user_client(request.user,False)):
        data['inicio']= 1
    elif (user_executive(request.user,False)):
        data['inicio']= 2
    elif (request.user.is_staff == True):
        data['inicio'] = 3
    
    data["request"] = request
    object_list = Rent.objects.all().order_by('-id')
    if(data['inicio']==1):
        users = User.objects.get(username = request.user)
        cli = Client.objects.get(user = users)
        print(cli.pk)
        object_list=Rent.objects.filter(client=cli.pk)
    

    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)

    template_name = 'list_rents.html'
    return render(request, template_name, data)


def rent_add(request,car_id):

    data = {}
    data['inicio'] = 0
    if (request.user.is_staff == True):
        data['inicio'] = 3
    elif (user_executive(request.user,False)):
        data['inicio']= 2
    #si es false el super admin no podra entrar
    if(user_client(request.user,False)):
        return redirect('cars')
    elif(data['inicio'] == 3):
        return redirect('list_rents')
    elif(data['inicio'] == 0):
        return redirect('cars')

    data["request"] = request
    if request.method == "POST":
        data['form'] = RentForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            us = Rent(start_date = request.POST["start_date"], end_date =request.POST["end_date"])
            cli = Client.objects.get(pk = request.POST["client"])
            users = User.objects.get(username = request.user)
            exe = Executive.objects.get(user = users)
            cars = Car.objects.get(pk = car_id)
            us.executive = exe
            us.car = cars
            us.client = cli
            us.save()

            return redirect('cars')

    else:
        data['form'] = RentForm()
                                
        
    template_name = 'add_rent.html'
    return render(request, template_name, data)

def edit_status(request, id, leter):
    #si es false el super admin no podra entrar
    data = {}
    template_name = 'list_rents.html'
    data["request"] = request
    arriendo = Rent.objects.get(pk=id)
    arriendo.status = leter
    arriendo.save()
    object_list = Rent.objects.all().order_by('-id')
    
    return HttpResponseRedirect(reverse('list_rents'))
