from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def index(request):
    context = {
        'none': None
    }
    return render(request, 'home/index.html', context)
