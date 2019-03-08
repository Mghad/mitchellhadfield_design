from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button

@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    context={}

    return render(request, 'mitchellhadfield_design/home.html', context)

def page(request):
    """
    Controller for the app home page.
    """
    context={}

    return render(request, 'mitchellhadfield_design/page.html', context)