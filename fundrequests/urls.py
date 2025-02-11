from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),  
    path("create/", create_fundraiser, name="create_fundraiser"),
    path("fundraiser/<int:fundraiser_id>/", fundraiser_detail, name="fundraiser_detail"),
    path("signup/", signup, name="signup"),
    path("login/", login_view, name="login"),
]
