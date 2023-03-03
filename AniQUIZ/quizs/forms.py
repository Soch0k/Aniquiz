from . import models
from django.forms import ModelForm, Textarea, ChoiceField, ModelChoiceField


class QuizForm(ModelForm):
    class Meta:
        model = models.Quiz

        fields = ['title', 'imageScreensaver', 'category', 'description']


class questionForm(ModelForm):
    class Meta:
        model = models.Questions

        fields = ['question', 'image', 'quiz']


class answerForm(ModelForm):
    class Meta:
        model = models.Answers

        fields = ['answer', 'correct', 'question_pk']


class ResultForm(ModelForm):
    class Meta:
        model = models.Results

        fields = ['quiz_pk', 'dict_answers', 'user', ]


class QuestionRedactForm(ModelForm):
    class Meta:
        model = models.Questions

        fields = ['question', 'image', ]
