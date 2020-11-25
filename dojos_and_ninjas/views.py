from .models import Dojo, Ninja
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    all_dojos = Dojo.objects.all()
    context = {
        'dojos': all_dojos,
    }
    return render(request, 'index.html', context)

def create_ninja(request):
    Ninja.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        temple = Dojo.objects.get(name = request.POST['place'])
    )
    return redirect('/')

def create_dojo(request):
    Dojo.objects.create(
        name = request.POST['name'],
        city = request.POST['city'],
        state = request.POST['state']
    )
    return redirect('/')