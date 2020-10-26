from django import forms
from django.core.exceptions import ValidationError
from .models import QuestionBox, AnswerBox


class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionBox
        fields = [
            'question',
        ]


class AnswerForm(forms.ModelForm):
    class Meta:
        model = AnswerBox
        fields = [
            'answer',
        ]


class SearchForm(forms.Form):
    question = forms.CharField(max_length=255)