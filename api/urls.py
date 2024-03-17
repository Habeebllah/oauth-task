from django.urls import path
from api.views import *
urlpatterns = [
    path('register/', GoogleSignupSocialAuthView.as_view()),
    path('login/', GoogleLoginSocialAuthView.as_view()),
]