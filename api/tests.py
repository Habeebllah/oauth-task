# tests.py

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()

# Fixtures for creating test data
@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user_data():
    return {
        'email': 'testuser@example.com',
        'password': 'testpassword',
    }

# Test for Google OAuth register endpoint
def test_google_oauth_register_api(api_client):
    # Assuming you have a separate view for handling Google OAuth registration
    url = reverse('google_register')
    # Mock the Google OAuth response
    mock_google_oauth_response = {
        {
         'status': "signup successful",
        'name': "Test Name",
        'email': "email@gmail.com",}
    }
    response = api_client.post(url, data=mock_google_oauth_response, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.filter(email='email@gmail.com').exists()

# Test for Google OAuth login endpoint
def test_google_oauth_login_api(api_client):
    # Assuming you have a separate view for handling Google OAuth login
    url = reverse('google_login')
    # Mock the Google OAuth response or use a testing tool like VCR
    mock_google_oauth_response = {
        'status': "login successful",
                'username': "Test Name",
                'email': "test@example.com",
                'tokens': {},
    }
    # Create a test user for the existing Google user
    user = User.objects.create_user(email='existinggoogleuser@example.com', password='testpassword')

    response = api_client.post(url, data=mock_google_oauth_response, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert 'token' in response.data