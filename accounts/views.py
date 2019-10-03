from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    # Some Var
    name = "Neuron Planets"
    numbers = [1, 2, 3]

    # Passing data to the html
    context = {
        'name': name,
        'numbers': numbers
    }

    return render(request, 'accounts/home.html', context)
