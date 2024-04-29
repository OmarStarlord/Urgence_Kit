from django.shortcuts import render



def mapping_view(request):
    return render(request, 'mapping.html')