from django.shortcuts import render, HttpResponse
from .models import GameShop
# Create your views here.
def index(request):
    return render(request, "index.html")

def index(request):
    oyunlar =  GameShop.objects.all()
    context = {
        'oyunlar': oyunlar
        
    }
    return render(request, 'index.html', context)