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


#Views Cars
@login_required(login_url='/auth/login')
def list_cars(request):
    #si es false el super admin no podra entrar
    if(user_client(request.user,False)):
        return redirect('cars')
    
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
    if(user_client(request.user,False) or user_executive(request.user,False)):
        return redirect('cars')
    data= {}
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
def delete_executive(request, id):
    #si es false el super admin no podra entrar
    if(user_client(request.user,False) or user_executive(request.user,False)):
        return redirect('cars')
    data = {}
    template_name = 'list_executives.html'
    data['executive'] = Executive.objects.all()
    User.objects.filter(pk=user_id).delete()
    Executive.objects.filter(pk=exe_id).delete()
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
    if(user_client(request.user,False)):
        return redirect('cars')
    data= {}
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
def delete_client(request, id):
    #si es false el super admin no podra entrar
    if(user_client(request.user,False)):
        return redirect('cars')
    data = {}
    template_name = 'list_clients.html'
    data['client'] = Client.objects.all()
    User.objects.filter(pk=user_id).delete()
    Client.objects.filter(pk=cli_id).delete()
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


#Views Arriendos
@login_required(login_url='/auth/login')
def list_rents(request):
    #si es false el super admin no podra entrar
    if(user_client(request.user,False)):
        return redirect('cars')
    
    data = {}
    
    rents = Rent.objects.all()
    # players = matchs.Player_set.all()
    for i in rents:
        print(i.car)
        print(i.client)
        print(i.executive)

    data["objects_list"] = rents
    template_name = 'list_rents.html'
    return render(request, template_name, data)

@login_required(login_url='/auth/login')
def rent_add(request):
    #si es false el super admin no podra entrar
    if(user_client(request.user,False)):
        return redirect('cars')
    data = {}
    data["request"] = request
    if request.method == "POST":
        data['form'] = RentForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('list_rents')

    else:
        data['form'] = RentForm()

    template_name = 'add_rent.html'
    return render(request, template_name, data)