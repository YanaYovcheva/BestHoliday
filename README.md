# BestHoliday

BestHoliday is a Django web application for discovering and booking excursions.  
The platform provides both a public section for browsing destinations and excursions,   
and a private section for authenticated users who can create bookings, manage favorites,   
and leave comments.

---

## Features

- User registration, login, and logout
- Extended custom user model with profile
- Public pages: Home, About, Contact
- Excursion browsing and detailed pages
- Destination and feature management
- Booking system
- Favorite excursions
- Comment system
- Role-based permissions with groups:
  - Managers
  - Support
- REST API for destinations
- Asynchronous task setup with Celery for booking confirmation emails

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- Celery
- Redis
- Bootstrap
- Pillow
- python-dotenv

## Project Structure

- `accounts` – authentication, custom user, profiles
- `common` – common pages and shared templates
- `excursions` – destinations, features, excursions
- `bookings` – bookings and favorites
- `reviews` – comments
- `tests` – project tests

## User Groups and Permissions

The project uses two user groups:

#### Managers  
Managers can manage:

Excursions
Destinations
Features
Support

#### Support
Support users can manage:

Comments
Bookings-related moderation tasks

These groups can be created and configured through the Django admin panel.

### Deployment not finished

## REST API

The project includes a REST API endpoint for destinations.

Example endpoints:

- GET /excursions/api/destinations/
- GET /excursions/api/destinations/int:pk/

## Installation

### 1. Clone the repository

```
git clone <https://github.com/YanaYovcheva/BestHoliday.git>
```

### 2.Create and activate a virtual environment
```
python -m venv .venv
.venv\Scripts\activate
```

### 3.Install dependencies
```
pip install -r requirements.txt
```

### 4.Configure environment variables
- Create a .env file like the example one
- Database setup - make sure PostgreSQL is installed and running 
- Then apply database migrations

### 5.Run the project
```
python manage.py runserver
```
By default, the server runs on http://127.0.0.1:8000/
