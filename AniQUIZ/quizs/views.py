from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import generic
from django.urls import reverse_lazy
from . import models, forms


class AniquizListView(ListView):
    model = models.Quiz
    template_name = "home.html"


def quizCreateView(request):
    errors = ''
    category = models.cateory
    if request.method == 'POST':
        form = forms.QuizForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('add_quiz_n', pk=post.pk)
        else:
            errors = form.errors

    data = {
        'errors': errors,
        'category': category,
    }
    return render(request, 'add_quiz.html', data)


def quizAdd_questions(request, pk):
    form = forms.questionForm
    errors = ''
    if request.method == 'POST':
        formQestion = forms.questionForm(request.POST, request.FILES)
        req=request.FILES
        if formQestion.is_valid():
            post = formQestion.save(commit=False, )
            post.quiz = pk
            post.save()
            return redirect('add_quiz_answers', pk=post.pk)
        else:
            errors = formQestion.errors
    data = {
        'form': form,
        'errors': errors,
        'quiz_pk': pk,
        'req': req,
    }
    return render(request, 'add_quiz.html', data)


#class quizAdd_questions(generic.CreateView):
#    form_class =forms.questionForm
#    success_url = reverse_lazy('add_quiz_answers')
#    template_name = 'add_quiz.html'



def quizAdd_answers(request, pk):

    errors = ''
    add_answer = models.answers.objects.filter(pk=pk)
    if request.method == 'POST':
        add_answer_form = forms.answerForm(request.POST)
        if add_answer_form.is_valid():
            add_answer_form.save()
            quiz_pk = models.questions.objects.filter(pk=pk)
            return redirect('add_quiz_n', pk=quiz_pk[1].pk)
        else:
            errors = add_answer.errors
    data = {
        'add_answer': add_answer,
        'errors': errors,
        'pk_question': pk,
    }
    return render(request, 'add_answers.html', data)



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
