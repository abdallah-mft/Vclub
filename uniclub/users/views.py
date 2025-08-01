from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserRegisterSerializer, UserSerializer , ProfilePictureSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated , AllowAny 
from rest_framework.parsers import MultiPartParser , FormParser 
from django.utils import timezone
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView

User = get_user_model()

class RegisterView(generics.CreateAPIView):   # This allows POST only 
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

class LogoutView(generics.GenericAPIView):
    class_permission = [IsAuthenticated]
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]   # refresh token is expected in the body 
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            user = User.objects.get(username=request.data['username'])
            user.last_login = timezone.now()
            user.save(update_fields=['last_login'])
        return response


class ProfilePictureView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)
    def patch(self,request):
        serializer = ProfilePictureSerializer(request.user,data=request.data,partial=True )

        if serializer.is_valid():
                serializer.save()
                return Response({"message": "Profile picture updated!", "profile_picture": serializer.data['profile_picture']})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)