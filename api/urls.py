from django.urls import path
from api.views import *
urlpatterns = [
    path('register/', GoogleSignupSocialAuthView.as_view(), name='google_register'),
    path('login/', GoogleLoginSocialAuthView.as_view(), name='google_login')
]