from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login as auth_login
from .forms import SignupForm, LoginForm
from .models import CustomUser
from .backends import CustomUserAuthenticationBackend
from chatbot.views import chatbot
from .forms import ProfileEditForm



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            phone = form.cleaned_data['phone']
            country = form.cleaned_data['country']
            city = form.cleaned_data['city']
            district = form.cleaned_data['district']

            user = CustomUser.objects.create_user(email=email, password=password, fullname=fullname, phone=phone, country=country, city=city, district=district)
            user.save()
            

            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)
                print("User logged in successfully.")
                #save session
                request.session['user_id'] = user.id
                request.session['user_email'] = user.email

                
                return redirect('chatbot:chatbot_home')  # Redirect to chatbot page upon successful login
            else:
                print("Invalid email or password.")
                error_message = "Invalid email or password."
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page upon logout



def edit_profile(request):
    user_id = request.session.get('user_id')
    if not user_id:
        # Handle case where user_id is not in session
        return render(request, 'error.html', {'message': 'User ID not found in session'})  # You can create a custom error template or handle this in your own way
    
    try:
        user = CustomUser.objects.get(pk=user_id)
    except CustomUser.DoesNotExist:
        # Handle case where user_id does not correspond to any user
        return render(request, 'error.html', {'message': 'User not found'})  # You can create a custom error template or handle this in your own way
    
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to profile page after successful edit
    else:
        form = ProfileEditForm(instance=user)

    return render(request, 'edit_profile.html', {'form': form})