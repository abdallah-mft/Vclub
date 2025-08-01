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
import random 


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

    def get(self, request):
        category =    request.query_params.get('category')
        wilaya   =    request.query_params.get('wilaya')
        shuffle_  =    request.query_params.get('shuffle','false').lower() == 'true' 

        queryset = Club.objects.all()     # queryset = many objects (rows)


        if category:
                queryset = queryset.filter(category=category) # list?category=Technology 
        if wilaya:
                queryset = queryset.filter(wilaya=wilaya) # list?wilaya=Medea 

        clubs = list(queryset.values())  # Turn queryset into queryset of dict but we django need list of dict so we use list  
            
        if shuffle_:
             random.shuffle(clubs) # shuffle() is a built in method in random that works with lists (clubs list in this case)

        return JsonResponse(clubs, safe=False, status=200) 




# V0.1 is ready ✔️




