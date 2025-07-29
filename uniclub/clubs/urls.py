from django.urls import path
from . import views
from .views import ClubRequestCreateView

urlpatterns = [
    path('request/', views.ClubRequestCreateView.as_view(), name='club-request'),
]
