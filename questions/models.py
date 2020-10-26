from django.db import models
from django.contrib.auth.models import User


class QuestionBox(models.Model):
    question = models.CharField(max_length=255)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

class AnswerBox(models.Model):
    answer = models.TextField()
    # question = models.ForeignKey('QuestionBox', on_delete=models.CASCADE)
    # favorites = models.ManyToManyField(User, related_name='favorites')  

    # @property
    # def numfavorites(self):
    #     return self.favorites.all().count()
