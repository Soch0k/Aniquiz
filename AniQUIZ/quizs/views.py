from django.shortcuts import render, redirect
from django.views.generic import ListView
from . import models, forms


class AniquizListView(ListView):
    model = models.Quiz
    template_name = "home.html"


def quizCreateView(request, pk):
    form = forms.QuizForm()
    hui = forms.QuizForm.objects.filter(pk=pk)
    errors = ''
    data = {}
    category = models.cateory
    if request.method == 'POST':
        form = forms.QuizForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('add_quiz_n', pk=post.pk)
        else:
            errors = form.errors

        data = {
            'form': form,
            'errors': errors,
        }
    else:
        data = {
            'forma': form,
            'errors': errors,
        }
    return render(request, 'add_quiz.html', data)


def quizAdd_questions(request, pk):
    form =


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
