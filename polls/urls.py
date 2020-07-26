from django.urls import path 
from .views import pollList, pollDetail

urlpatterns = [
    path('polls', pollList, name="poll_list"),
    path('polls/<int:pk>/', pollDetail, name="poll_detail"),
]
