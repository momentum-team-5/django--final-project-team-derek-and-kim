from django.db import models
from django.contrib.auth.models import User


class QuestionBox(models.Model):
    question = models.CharField(max_length=255)
    # timestamp = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # favorites = models.ManyToManyField(User, related_name='favorites')

class AnswerBox(models.Model):
    answer = models.TextField()
    # timestamp = models.DateTimeField(auto_now_add=True)
    # question = models.ForeignKey('QuestionBox', on_delete=models.CASCADE)

    # @property
    # def numfavorites(self):
    #     return self.favorites.all().count()
