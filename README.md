## Simple Django RESTful API for User Registration and Login Using Google OAuth

# Installation steps

1. Ensure you have python3 installed

2. Clone the repository

3. create a virtual environment using `python -m venv <name>`

4. Activate the virtual environment by running `source scripts/activate`

5. Install the dependencies using `pip install -r requirements.txt`

6. Migrate existing db tables by running `python manage.py migrate`

7. Run the django development server using `python manage.py runserver`

# Project Features
- Creation of a Django project with a RESTful API for user registration and login using Google OAuth.
- Available endpoints:
    ```
    /api/register/: Register a new user using OAuth.
    /api/login/ : Login an existing user using OAuth.

    <id_token> is the required payload to be passed endpoints from the Frontend
    ```
- PostgreSQL database is utilized.
- Implementation of logging to record API requests and responses.
- Effective Use Django's serializers for data validation and serialization.
- Implement rate limiting for the API endpoints.

# Setting up .env variables
```
GOOGLE_CLIENT_ID = <>
GOOGLE_CLIENT_SECRET = <>
SOCIAL_SECRET = <>
POSTGRESQL_USER = <>
POSTGRESQL_PASSWORD = <>
```