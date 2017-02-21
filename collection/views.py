from django.shortcuts import render

# Create your views here.
def index(request): 
    thing = "Thing name"
    # this is your new view
    return render(request, 'index.html', { 
        'thing': thing,
    })