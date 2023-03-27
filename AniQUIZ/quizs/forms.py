from . import models
from django.forms import ModelForm
from django import forms


class QuizForm(ModelForm):
    class Meta:
        model = models.Quiz

        fields = ['title', 'imageScreensaver', 'category', 'description']


class questionFormWithImg(ModelForm):
    class Meta:
        model = models.Questions

        fields = ['question', 'image', 'quiz']


class questionFormWithoutImg(ModelForm):
    class Meta:
        model = models.Questions

        fields = ['question', 'quiz']


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

        widgets = {
            "question": forms.TextInput(attrs={
                'id': 'question_name',
            }),
            "image": forms.FileInput(attrs={
                'id': 'question_image',
            }),
        }

        fields = ['question', 'image', ]


class AnswerRedactForm(ModelForm):
    class Meta:
        model = models.Answers

        widgets = {
            "answer": forms.TextInput(attrs={
                'id': 'Answer',
            }),
        }

        fields = ['answer', 'correct']
