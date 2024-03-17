from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import GoogleTokenSerializer
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth import authenticate, login

class GoogleLoginView(APIView):
    def post(self, request):
        serializer = GoogleTokenSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.validated_data.get('token')
            user = authenticate(google_auth_token=token)
            if user:
                login(request, user)
                return Response({'message': 'Login successful'})
            else:
                return Response({'message': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GoogleSignupView(APIView):
    def post(self, request):
        serializer = GoogleTokenSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.validated_data.get('token')
            # Get user info from Google using the token
            # For example:
            # social_account = SocialAccount.objects.get(token=token)
            # email = social_account.extra_data.get('email')
            # Create user account with retrieved info
            # user = User.objects.create(email=email, ...)
            # user.save()
            # Then authenticate and login the user
            # login(request, user)
            return Response({'message': 'Signup successful'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
