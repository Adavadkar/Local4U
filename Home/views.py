from http.client import HTTPResponse

from django.shortcuts import render,  redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from Home.models import Category
from LocalFarmers.models import Farmer
from django.contrib.auth.decorators import login_required
from .models import Profile
# Create your views here.
def index(request):
    categories = Category.objects.all()
    farmers = Farmer.objects.all()
    return render(request, 'index.html', {'categories': categories, 'farmers': farmers})


def signup_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        contact_number = request.POST.get('contact_number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user_type = request.POST.get('user_type')  # Get user type from form

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('login')

        # Create user and profile
        user = User.objects.create_user(username=username, password=password, email=email)
        Profile.objects.create(user=user, user_type=user_type)

        messages.success(request, "Account created successfully. Please log in.")
        return redirect('login')  # Redirect to login page after signup

    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Adjust based on your homepage URL
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('login')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def farmer_dashboard(request):
    if request.user.profile.user_type != 'farmer':
        return redirect('home')
    # Farmer-specific content here
