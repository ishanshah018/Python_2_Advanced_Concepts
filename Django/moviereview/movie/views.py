from django.shortcuts import render
from .models import Movie

# Create your views here.

def Home(request):
    searchTerm=request.GET.get('searchMovie')
    
    if searchTerm:
        movies=Movie.objects.filter(title__icontains=searchTerm)
        
    else:
        movies=Movie.objects.all()
        
    return render(request,'home.html',{'searchTerm':searchTerm,'movies':movies})