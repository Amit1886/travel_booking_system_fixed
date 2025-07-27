# travel_system/apps/accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # <-- add this
    # other URLs...
]
