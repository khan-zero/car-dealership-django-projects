from django.shortcuts import render
from .models import WellcomeHerro, Vehicles, Services, ClientsReviews, Partner
# Create your views here.

from django.shortcuts import render
from .models import WellcomeHerro, Vehicles, Services, ClientsReviews, Partner, TopBrands

def index(request):
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
        'client_reviews': client_reviews,
        'partners': partners,
        'top_brands': top_brands,
    }

    return render(request, 'index.html', context)



