from django.shortcuts import render, redirect
from django.http import HttpResponse
import folium
import geocoder
from .models import Search
from .forms import SearchForm

def map(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            address = form.cleaned_data['address']  # Retrieve the submitted address
            location = geocoder.osm(address)
            lat = location.lat
            lng = location.lng
            country = location.country
            if lat is None or lng is None:
                return HttpResponse('Your address input is invalid')
            else:
                m = folium.Map(location=[lat, lng], zoom_start=10)
                folium.Marker([lat, lng], tooltip='Click for more', popup=country).add_to(m)
                m = m._repr_html_()
                context = {'m': m, 'form': form}
                return render(request, 'map.html', context)
    else:
        form = SearchForm()
    
    context = {'form': form}
    return render(request, 'map.html', context)
