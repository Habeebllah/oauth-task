from django.urls import path
from .views import GoogleLoginView, GoogleSignupView

urlpatterns = [
    path('api/google/login/', GoogleLoginView.as_view(), name='google_login'),
    path('api/google/signup/', GoogleSignupView.as_view(), name='google_signup'),
]
