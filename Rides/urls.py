from django.urls import path
from . import views
# from . import consumers  # Import the consumers module

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('safety', views.safety, name='safety'),
    path('login_form', views.login_form, name='login_form'),
    path('signup', views.signup, name='signup'),
    path('signupasdriver', views.signupasdriver, name='signupasdriver'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('bookride', views.bookride, name='bookride'),

    # path('ws/ridenotifications/', consumers.RideNotificationConsumer.as_asgi()),
    path('acceptride/<int:ride_id>/', views.acceptride, name='acceptride'),
    path('cancelride/<int:ride_id>/', views.cancelride, name='cancelride'),
]