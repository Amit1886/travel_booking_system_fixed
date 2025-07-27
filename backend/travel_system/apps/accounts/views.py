# TODO: implement views
# travel_system/apps/accounts/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to Travel Booking System</h1>")
