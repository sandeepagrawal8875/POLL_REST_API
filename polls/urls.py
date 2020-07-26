from django.urls import path

from .views import PollList, PollDetail
# from .views import pollList, pollDetail


"""function based"""
# urlpatterns = [
#     path('polls', pollList, name="poll_list"),
#     path('polls/<int:pk>/', pollDetail, name="poll_detail"),
# ]

"""classed base"""
urlpatterns = [
    path("polls/", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
]
