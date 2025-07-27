
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('travel_system.apps.accounts.urls')),
    path('bookings/', include('travel_system.apps.bookings.urls')),
    path('payments/', include('travel_system.apps.payments.urls')),
]
