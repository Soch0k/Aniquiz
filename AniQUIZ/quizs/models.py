from django.db import models
from django.urls import reverse
from django.conf import settings
from picklefield.fields import PickledObjectField

class cateory(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name[:20]


class Quiz(models.Model):
    title = models.CharField(max_length=128, null=True, default='none')
    imageScreensaver = models.ImageField(upload_to="static/img/quizs_img/imageScreensavers", null=True, default='static/img/quizs_img/imageScreensavers/47899679c157cb3b7fb73e2134086efb.jpg')
    category = models.ForeignKey(cateory, on_delete=models.CASCADE, null=True, default=1)
    status = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    popular = models.IntegerField(default=0)

    def get_absolut_url(self):
        return reverse('add_quiz_n', args=[str(self.id)])

    def __str__(self):
        return self.title[:20]


class Questions(models.Model):
    question = models.CharField(max_length=64)
    image = models.ImageField(upload_to="static/img/quizs_img/questions_img", null=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.question[:20]


class Answers(models.Model):
    answer = models.CharField(max_length=128, null=True)
    correct = models.BooleanField()
    question_pk = models.ForeignKey(Questions, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer[:20]


class Dict(models.Model):
    key = models.CharField(max_length=24)
    value = models.CharField(max_length=24)


class Results(models.Model):
    quiz_pk = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    dict = models.ForeignKey(Dict, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.dict[:20]

