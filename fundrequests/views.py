from django.shortcuts import render,get_object_or_404,redirect
from .models import Fundraiser  
from .forms import FundraiserForm
from django.contrib import messages  
from django.contrib.auth.decorators import login_required


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

