from django.shortcuts import render
from rest_framework import generics, permissions
from .models import ClubRequest
from .serializers import ClubRequestSerializer
from rest_framework.permissions import IsAuthenticated

# Anyone can send a club creation request
class ClubRequestCreateView(generics.CreateAPIView): # This allows POST only 
    queryset = ClubRequest.objects.all()
    serializer_class = ClubRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Save the user who sent the request, for example
        serializer.save()

