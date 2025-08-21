pip install -r .\requirements.txt - to download dependencies
http://127.0.0.1:8000/ "Index page"
/bookings/
/api/menu-items/
/api/menu-items/<int:pk>/
/api/api-token-auth/
/auth/users/
/auth/users/me/
/auth/token/login/

🍋 Little Lemon Restaurant API & Website

This project is a restaurant web application and REST API built with Django and Django REST Framework.
It includes a frontend (HTML templates) for restaurant promotion and an API for managing menu items and bookings.

🚀 Features

Public restaurant website with static pages (home, menu, booking, about).

REST API with CRUD operations for Menu Items and Bookings.

Token-based authentication (/api-token-auth/).

Protected API views (accessible only to authenticated users).

Unit tests for API endpoints.

🔗 Main URLs
Website

/ → Home page

/menu/ → Menu (API view)

/bookings/ → Booking API

API

/menu-items/ → List and create menu items (auth required)

/menu-items/<id>/ → Retrieve, update or delete menu item

/message/ → Protected test endpoint (auth required)

/api-token-auth/ → Get authentication token
HTML + CSS (templates, with Google Fonts)
