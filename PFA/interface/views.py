from django.shortcuts import render
from .models import Tip, NutrimentAndSupply, EmergencyContact

def home(request):
    return render(request, 'home.html')

def fill_sections(request):
    if request.method == 'POST':
        country = request.POST.get('country')
        type_of_catastrophe = request.POST.get('incident-type')

        tips = Tip.objects.filter(type_of_catastrophe=type_of_catastrophe)
        tips = tips.order_by('?')[:5]
        nutriments_and_supplies = NutrimentAndSupply.objects.filter(type_of_catastrophe=type_of_catastrophe)
        nutriments_and_supplies = nutriments_and_supplies.order_by('?')[:5]
        print(country)
        emergency_contacts = EmergencyContact.objects.filter(country=country)


        return render(request, 'filled_sections.html', {
            'tips': tips,
            'nutriments_and_supplies': nutriments_and_supplies,
            'emergency_contacts': emergency_contacts
        })
    else:
        return render(request, 'home.html')