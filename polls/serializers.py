from rest_framework import serializers

from .models import Poll, Choice, Vote

class VoteSerializer(serializers.ModelSerializer):
    """convert vote model to json data"""
    
    class Meta:
        model = Vote
        fields = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):
    """Choice model to Json data"""

    votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Choice
        fields = '__all__'
    
class PollSerializer(serializers.ModelSerializer):
    """Poll serializers"""
    Choice = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Poll
        fields = '__all__'
