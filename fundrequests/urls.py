from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  
    path("create/", views.create_fundraiser, name="create_fundraiser"),
    path("fundraiser/<int:fundraiser_id>/", views.fundraiser_detail, name="fundraiser_detail"),
]
