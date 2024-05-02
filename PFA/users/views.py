from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import SignupForm, LoginForm
from .models import CustomUser
from chatbot.views import chatbot
from .forms import ProfileEditForm

from django.contrib.auth import logout





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
            

            return redirect('users:login')
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
                # Save session
                request.session['user_id'] = user.id
                request.session['user_email'] = user.email
                return redirect('home')  
            else:
                print("Invalid email or password.")
                error_message = "Invalid email or password."
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def user_logout(request):
    print("User logged out successfully.")
    logout(request)
    request.session.flush()
    return redirect('users:login')  


def edit_profile(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return render(request, 'error.html', {'message': 'User ID not found in session'})
    
    try:
        user = CustomUser.objects.get(pk=user_id)
    except CustomUser.DoesNotExist:
        return render(request, 'error.html', {'message': 'User not found'})
    
    if request.method == 'POST':
        # Handle form submission
        # Retrieve form data from POST request
        name = request.POST.get('name')
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_new_password = request.POST.get('confirm_new_password')
        current_email = request.POST.get('current_email')
        new_email = request.POST.get('new_email')
        confirm_new_email = request.POST.get('confirm_new_email')

        # Your logic to update user profile goes here
        # For example:
        if current_password == user.password:  # Assuming user.password stores the current password
            # Update user information based on form data
            user.name = name
            user.email = new_email
            
            user.save()
            return redirect('profile')  # Redirect to profile page after successful edit
        else:
            # Handle incorrect password scenario or any other validation errors
            # For simplicity, let's render the edit_profile.html template again with an error message
            error_message = "Incorrect password"
            return render(request, 'edit_profile.html', {'error_message': error_message})

    # If request method is GET, render the edit_profile.html template with user information
    return render(request, 'edit_profile.html', {'user': user})