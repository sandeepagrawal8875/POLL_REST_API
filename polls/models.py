from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    """creating question in polls"""
    question = models.CharField(max_length=200)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question[:20]


class Choice(models.Model):
    """choice for question"""
    poll = models.ForeignKey(to=Poll, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)

    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    """Voting database"""
    choice = models.ForeignKey(to=Choice, on_delete=models.CASCADE)
    poll = models.ForeignKey(to=Poll, on_delete=models.CASCADE)
    voted_by = models.ForeignKey(to=User, on_delete=models.Model)

    class Meta:
        unique_together = ("poll", "voted_by")