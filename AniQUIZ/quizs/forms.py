from . import models
from django.forms import ModelForm, Textarea, ChoiceField, ModelChoiceField


class QuizForm(ModelForm):
    class Meta:
        model = models.Quiz

        fields = ['title', 'imageScreensaver', 'category']


class questionForm(ModelForm):
    class Meta:
        model = models.questions

        fields = ['question', 'image', 'quiz']