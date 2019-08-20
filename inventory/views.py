from django.shortcuts import render
from inventory.models import * 

# Create your views here.

def index(request):
    artists = Artist.objects.all()
    # return HttpResponse("Hello world! Inventory index!")

    return render(request, "inventory/index.html", locals())
