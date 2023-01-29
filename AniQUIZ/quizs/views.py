from django.shortcuts import render, redirect
from django.views.generic import ListView
from . import models, forms


class AniquizListView(ListView):
    model = models.Quiz
    template_name = "home.html"


def quizCreateView(request):
    form = forms.QuizForm
    errors = ''
    if request.method == 'POST':
        form = forms.QuizForm
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            errors = form.errors

    data = {
        'form': form,
        'errors': errors,
    }
    return render(request, 'add_quiz.html', data)


def addQuestion(request):
    form = forms.questionForm
    errors = ''
    if request.method == 'POST':
        form = forms.questionForm
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            errors = form.errors
    data = {
        'errors': errors,
        'form': form,
    }
    return render(request, 'add_quiz.html', data)