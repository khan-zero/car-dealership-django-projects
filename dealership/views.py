from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse

from .forms import UserRegistrationForm
from .models import WellcomeHerro, Vehicles, Services, ClientsReviews, Partner, TopBrands
#from .decorators import unauthorized_user, allowed_users, admin_only


#wrappers:
def unauthorized_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not authorized to view this page.")
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == "customer":
            return redirect('user-page')
        elif group == "admin":
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse("You are not authorized to view this page.")
    return wrapper_func



#views -------------------------------------------------------------------------------------------------------------






from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse

from .forms import UserRegistrationForm
from .models import WellcomeHerro, Vehicles, Services, ClientsReviews, Partner, TopBrands
#from .decorators import unauthorized_user, allowed_users, admin_only


@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')


def info(request):
    # Fetch all hero objects
    heroes = WellcomeHerro.objects.all()

    # Fetch distinct values for each field
    years = Vehicles.objects.values_list('year', flat=True).distinct()
    bodies = Vehicles.objects.values_list('body', flat=True).distinct()
    manufacturers = Vehicles.objects.values_list('manufactor', flat=True).distinct()
    models = Vehicles.objects.values_list('model', flat=True).distinct()
    conditions = Vehicles.objects.values_list('condition', flat=True).distinct()

    # Get the 3 latest vehicles ordered by year
    latest_vehicles = Vehicles.objects.order_by('-year')[:3]

    # Fetch services, client reviews, and partners, more..
    services = Services.objects.all()
    client_reviews = ClientsReviews.objects.all()
    partners = Partner.objects.all()
    top_brands = TopBrands.objects.all()

    # Create context to pass to the template
    context = {
        'heroes': heroes,
        'years': years,
        'bodies': bodies,
        'manufacturers': manufacturers,
        'models': models,
        'conditions': conditions,
        'latest_vehicles': latest_vehicles,
        'services': services,
        'clients_reviews': client_reviews,
        'partners': partners,
        'top_brands': top_brands,
    }

    return render(request, 'info.html', context)

@admin_only
def dashboard(request):

    welcome = WellcomeHerro.objects.all()
    vehicles = Vehicles.objects.all()
    services = Services.objects.all()
    client_reviews = ClientsReviews.objects.all()
    partners = Partner.objects.all()
    top_brands = TopBrands.objects.all()
    
    context = {
        'wellcome_herro':welcome,
        'vehicles':vehicles,
        'services':services,
        'client_reviews':client_reviews,
        'partners':partners,
        'top_brands':top_brands,
    }


    return render(request, 'dashboard.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('info')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid form submission.')
    else:
        form = AuthenticationForm()
        
    return render(request, 'login.html', {f'form': form})

def logout_view(request):
    logout(request)
    return redirect('info')
    
def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Registration successful.')
            return redirect('login')
        else:
            messages.error(request, 'Invalid form submission.')
    else:
        form = UserRegistrationForm()
        
    return render(request, 'register.html', {'form': form})
