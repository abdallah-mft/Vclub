from django.shortcuts import render
from rest_framework import generics, permissions
from .models import ClubRequest
from .serializers import ClubRequestSerializer
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSearchSerializer
from users.models import CustomUser
from rest_framework.views import APIView
from .models import Club
from django.http import JsonResponse
from django.views import View


# Anyone can send a club creation request
class ClubRequestCreateView(generics.CreateAPIView): # This allows POST only 
    queryset = ClubRequest.objects.all()
    serializer_class = ClubRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Save the user who sent the request, for example
        serializer.save()

class UserSearchView(generics.ListAPIView):
    serializer_class = UserSearchSerializer 
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('search','') 
        return CustomUser.objects.filter(username__icontains=query)[:5]
    
class ClubList(APIView):
    permission_classes = [IsAuthenticated]

    def get (self, request):
        category = request.query_params.get('category')
        if category : 
            clubs = list(Club.objects.filter(category=category).values())
        else:
            clubs = list(Club.objects.values())
        return JsonResponse(clubs, safe=False , status = 200 )
        


    


