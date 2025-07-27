
# Travel & Car Booking System

This is a minimal Django-based car booking system skeleton with role management, Razorpay test integration stubs, Google Maps placeholder, and WhatsApp mock alerts.

## Setup (VS Code)

1. Create virtual env and install requirements:
    ```
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

2. Create MySQL database `travel_db` and import `sql/travel_booking_system.sql` if provided.

3. Update `backend/travel_system/settings.py` database credentials.

4. Run migrations and create superuser:
    ```
    python backend/manage.py makemigrations
    python backend/manage.py migrate
    python backend/manage.py createsuperuser
    ```

5. Run development server:
    ```
    python backend/manage.py runserver
    ```

## Payments

Fill your Razorpay test keys in environment variables and integrate inside `travel_system/apps/payments`.

## Google Maps & WhatsApp

Replace placeholder comments with real API keys and logic.

## Frontend

Basic static HTML is in `frontend/`. You can integrate it with Django templates or serve separately via React/JS.
