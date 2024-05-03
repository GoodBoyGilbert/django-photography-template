from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="hello_world"),
    path("detail/<int:image_id>", views.detail, name="detail"),
    path("about",views.about,name="about"),
    path("services",views.services, name="services"),
    path("contact",views.contact, name="contact"),
    path("gallery",views.gallery, name="gallery")
]
