from django.db import models
from users.models import User


class QuestionBox(models.Model):
    question = models.CharField(max_length=255, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)


class AnswerBox(models.Model):
    answer = models.TextField()
    question = models.ForeignKey('QuestionBox', on_delete=models.CASCADE, null=True, related_name='answers')
    favoriting_users = models.ManyToManyField(User, related_name='favorite_answers')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)  

    def numfavorites(self):
        return self.favoriting_users.count()
