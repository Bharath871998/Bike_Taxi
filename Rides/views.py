from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import SignUpForm, LoginForm, DriverSignUpForm, BookrideForm
from .models import Customer, Driver, BookRide
from django.contrib.auth.hashers import check_password
# from django.core.mail import send_mail  # For email notifications
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import json

# Create your views here.
def home(request):
    username = request.session.get('username')
    if username:
        context = {'username': username}
        return render(request, "home.html", context)
    return  render(request, "home.html")

def aboutus(request):
    username = request.session.get('username')
    if username:
        context = {'username': username}
        return render(request, "aboutus.html", context)
    return  render(request, "aboutus.html")

def safety(request):
    username = request.session.get('username')
    if username:
        context = {'username': username}
        return render(request, "safety.html", context)
    return  render(request, "safety.html")


# Driver Sign-up view
def signupasdriver(request):
    if request.method == 'POST':
        form = DriverSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for Driver {username}!')
            return redirect('login_form')  # Replace 'home' with the name of your home page URL
    else:
        form = DriverSignUpForm()
    return render(request, 'driver_signup.html', {'form': form})


# Customer sign-up view
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login_form')  # Replace 'home' with the name of your home page URL
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


# Customer and Driver Login view
def login_form(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Trying to find whether the user is customer or driver 
            user = None
            try:
                user = Customer.objects.get(username=username)
                if check_password(password, user.password):
                    # request.session['user_id'] = user.id
                    request.session['username'] = user.username
                    request.session['is_customer'] = True
                    # print(messages.success(request, f'{user.username} You have been logged in successfully.'))
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid username or password.')
            except Customer.DoesNotExist:
                # messages.error(request, 'Invalid username or password.')
                pass

            try:
                driver = Driver.objects.get(username=username)
                if check_password(password, driver.password):
                    # request.session['user_id'] = user.id
                    request.session['username'] = driver.username
                    request.session['is_driver'] = True
                    # print(messages.success(request, f'{driver.username}, You have been logged in successfully as Driver'))
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid username or password.')
            except Driver.DoesNotExist:
                # messages.error(request, 'Invalid username or password.')
                pass
            # If neither a customer nor a driver is found
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, "login_form.html", {'form': form})



def logout_view(request):
    request.session.flush()
    return redirect('home')  


# def bookride(request):
#     username = request.session.get('username')
#     if username:
#         customer = Customer.objects.get(username=username)  # Fetch the customer object
#         if request.method == 'POST':
#             form = BookrideForm(request.POST)
#             if form.is_valid():
#                 ride = form.save(commit=False)
#                 ride.customer = customer  # Set the customer field
#                 ride.status = 'waitng'
#                 ride.save()
#                 source = form.cleaned_data['source']
#                 destination = form.cleaned_data['destination']
#                 messages.success(request, f'Hey {username}!, Your ride is booked from {source} to {destination}')
#                 return redirect('bookride')
#             else:
#                 messages.success(request, f'Hey {username}!, Sorry, your ride is cancelled from {source} to {destination}')
#         else:
#             initial_status = {'ride_status': 'Waiting'}  # Set initial status to 'booked'
#             form = BookrideForm(initial=initial_status)
#             context = {'username': username, 'form': form}
#         return render(request, 'bookride.html', context)
#     else:
#         return render(request, 'login_form')
    


def bookride(request):
    username = request.session.get('username')
    if username:
        customer = Customer.objects.get(username=username)  # Fetch the customer object
        if request.method == 'POST':
            form = BookrideForm(request.POST)
            if form.is_valid():
                ride = form.save(commit=False)
                ride.customer = customer  # Set the customer field
                ride.ride_status = 'waiting'
                ride.save()

                channel_layer = get_channel_layer()
                async_to_sync(channel_layer.group_send)(
                    "drivers",
                    {
                        "type": "ridenotification",
                        "message": {
                            "text": f"New ride from {ride.source} to {ride.destination}.",
                            "id": ride.id
                        }
                    }
                )
                
                messages.success(request, f'Hey {username}! Your ride is booked from {ride.source} to {ride.destination}. Waiting for a driver to accept.')
                return redirect('bookride')
            else:
                messages.error(request, 'Failed to book the ride. Please try again.')
        else:
            form = BookrideForm()
        return render(request, 'bookride.html', {'form': form, 'username': username})
    else:
        return redirect('login_form')



def acceptride(request, ride_id):
    ride = BookRide.objects.get(pk=ride_id)
    if request.method == 'POST':
        ride.ride_status = 'accepted'
        ride.driver = request.user.driver  # Assuming driver is related to user
        ride.save()
        return HttpResponse("Ride accepted")
    return render(request, 'accept_ride.html', {'ride': ride})

def cancelride(request, ride_id):
    ride = BookRide.objects.get(pk=ride_id)
    if request.method == 'POST':
        ride.ride_status = 'cancelled'
        ride.save()
        return HttpResponse("Ride cancelled")
    return render(request, 'cancel_ride.html', {'ride': ride})

