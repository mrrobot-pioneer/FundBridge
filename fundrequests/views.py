from django.shortcuts import render,get_object_or_404,redirect
from .models import Fundraiser  
from .forms import FundraiserForm,SignupForm,LoginForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])  
            user.save()

            login(request, user)  # Log in the user after signup
            messages.success(request, "Signup successful! Welcome to FundBridge.")
            return redirect("home")  

        else:
            messages.error(request, "Error signing up. Please check your details and try again!")
    else:
        form = SignupForm()

    return render(request, "signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect("home")  
            else:
                messages.error(request, "Invalid username or password. Please try again.")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


def home(request):
    # Fetch the latest 10 approved fundraisers, ordered by the most recent
    fundraisers = Fundraiser.objects.filter(approved=True).order_by('-created_at')[:10]
    return render(request, "home.html", {"fundraisers": fundraisers})


@login_required(login_url="login")  # Redirects to login page if user is not logged in
def create_fundraiser(request):
    if request.method == "POST":
        form = FundraiserForm(request.POST, request.FILES)
        if form.is_valid():
            fundraiser = form.save(commit=False)
            fundraiser.created_by = request.user  # Associate fundraiser with logged-in user
            fundraiser.save()

            messages.success(request, "Your fundraiser has been created successfully!")

            return redirect("home")  
        else:
            messages.error(request, "There was an error submitting the form. Please try again.")

    else:
        form = FundraiserForm()

    return render(request, "fundraiser.html", {"form": form})


def fundraiser_detail(request, fundraiser_id):
    fundraiser = get_object_or_404(Fundraiser, id=fundraiser_id)
    return render(request, "fundraiser_details.html", {"fundraiser": fundraiser})

