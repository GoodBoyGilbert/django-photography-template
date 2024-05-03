from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Image

# Create your views here.

def index(request):
  image = Image.objects.all
  return render(request, "index.html", {'Image' : image})

def detail(request, image_id):
  image = get_object_or_404(Image, pk=image_id)
  return render(request, "detail.html", {"image":image})

def about(request):
  return render(request, "about.html")

def services(request):
  return render(request, "services.html")

def contact(request):
  return render(request, "contact.html")

def gallery(request):
  image = Image.objects.all
  return render(request,"gallery.html", {"Image":image})