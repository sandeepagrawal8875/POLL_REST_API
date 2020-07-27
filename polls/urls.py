from django.urls import path

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import (PollViewSet,
                    PollDetail,
                    ChoiceList, 
                    CreateVote,
                    UserCreate,
                    LoginView)



"""viewset Based urls"""

router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')

urlpatterns = [
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="created_vote"),
    path("users/", UserCreate.as_view(), name="users"),
    path("login/", LoginView.as_view(), name="login")
]

urlpatterns += router.urls


"""classed base"""
# from .views import PollList, PollDetail, ChoiceList, CreateVote

# urlpatterns = [
#     path("polls/", PollList.as_view(), name="polls_list"),
#     path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
#     path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
#     path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="created_vote"),
# ]


"""function based"""
# from .views import pollList, pollDetail
 
# urlpatterns = [
#     path('polls', pollList, name="poll_list"),
#     path('polls/<int:pk>/', pollDetail, name="poll_detail"),
# ]