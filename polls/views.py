from rest_framework import generics

# from django.shortcuts import get_object_or_404
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from django.http import JsonResponse


from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer
from .models import Poll, Choice, Vote



"""Generics classed based view"""

class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


"""APIView classed based view"""

# class PollList(APIView):
#     def get(self, request):
#         polls = Poll.objects.all()[:20]
#         data = PollSerializer(polls, many=True).data
#         return Response(data)

# class PollDetail(APIView):
#     def get(self, request, pk):
#         poll = get_object_or_404(Poll, pk=pk)
#         data = PollSerializer(poll).data
#         return Response(data)

"""function based"""

# def pollList(request):
#     MAX_OBJECTS = 20
#     polls = Poll.objects.all()[:MAX_OBJECTS]
#     data = { "results" : list(polls.values("question", "created_by__username", "pub_date")) }
    
#     return JsonResponse(data)

# def pollDetail(request, pk):
#     poll = get_object_or_404(Poll, id=pk)
#     data = { "result": {
#         "question": poll.question,
#         "created_by": poll.created_by.username,
#         "pub_date": poll.pub_date
#     }}
#     return JsonResponse(data)
