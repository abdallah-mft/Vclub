from django.urls import path
from . import views
from .views import ClubRequestCreateView , ClubList

urlpatterns = [
    path('request/', views.ClubRequestCreateView.as_view(), name='club-request'),
    path('list/', views.ClubList.as_view(), name='club-list'),
]