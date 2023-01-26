from django.db import models


class cateory(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name[:20]

class Quiz(models.Model):
    title = models.CharField(max_length=128)
    imageScreensaver = models.ImageField(upload_to="static/img/quizs_img/imageScreensavers", null=True),
    category = models.ForeignKey(cateory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title[:20]


class questions(models.Model):
    question = models.CharField(max_length=64)
    image = models.ImageField(upload_to="static/img/quizs_img/questions_img", null=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.question[:20]


class answers(models.Model):
    answer = models.CharField(max_length=128)
    correct = models.BooleanField()
    questions = models.ForeignKey(questions, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer[:20]
