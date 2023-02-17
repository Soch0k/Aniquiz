from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import generic, View
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from . import models, forms
import json


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
        if formQestion.is_valid():
            post = formQestion.save(commit=False)
            post.save()
            return redirect('add_quiz_answers', pk=post.pk)
        else:
            errors = formQestion.errors
    data = {
        'questions': models.Questions.objects.filter(quiz=pk),
        'form': form,
        'errors': errors,
        'quiz_pk': pk,
    }
    return render(request, 'add_quiz.html', data)


# class quizAdd_questions(generic.CreateView):
#    form_class =forms.questionForm
#    success_url = reverse_lazy('add_quiz_answers')
#    template_name = 'add_quiz.html'


def quizAdd_answers(request, pk):
    errors = ''

    if request.method == 'POST':
        inp = 'ичто ты смотришь сюда?'
        print(request.POST)
        print(len(request.POST))

        req = request.POST

        for key in request.POST:
            print(req[key])
            if key[:-1] == 'answer':
                if key == req['correct']:
                    post = models.Answers.objects.create(
                        answer=req[key],
                        question_pk_id=pk,
                        correct=1,
                    )
                    post.save()
                else:
                    post = models.Answers.objects.create(
                        answer=req[key],
                        question_pk_id=pk,
                        correct=0,
                    )
                    post.save()

        # pk_qst =
        return redirect('add_quiz_n', pk)
    data = {
        'pk_question': pk,
    }
    return render(request, 'add_answers.html', data)

    # answer = request.POST.get('answer')
    # correct = request.POST.get('correct')
    # question_pk = request.POST.get('question_pk')

    # for i in request.POST.get('quantity'):
    #    post = models.answers.objects.create(
    #        answer=request.POST.get('answer' + str(i)),
    #        correct=1,
    #        question_pk=request.POST.get('question_pk' + str(i)),
    #    )

    # post = models.answers.objects.create(
    #    answer=answer,
    #    correct=correct,
    #    question_pk_id=pk,
    # )
    #
    # post.save()
    # return redirect('home')


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


# def is_ajax(request):
#    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def quizView(request, pk):
    form = models.Quiz.objects.filter(pk=pk)
    questions = models.Questions.objects.filter(quiz=form[0].pk)
    answers = models.Answers
    data = {
        'pkQuiz': pk,
        'quiz': form,
        'questions': questions,
        'answers': answers,
    }

    return render(request, 'quiz.html', data)


def returnThisQuestion(request, quiz, num):
    try:
        Question = list(models.Questions.objects.values('question', 'image', 'quiz').filter(quiz=quiz))[int(num)]
        takePkQuestionForAnswers = models.Questions.objects.filter(quiz=quiz)
        answers = list(models.Answers.objects.values('answer', 'correct', 'question_pk').filter(
            question_pk=takePkQuestionForAnswers[int(num)].pk))

        return JsonResponse({'Question': Question, 'Answers': answers})
    except:
        return JsonResponse()

    # question = models.Questions.objects.filter(quiz=quiz)
    # answers = models.Answers.objects.filter(question_pk=question[0].id)
    # data = {
    #    'questions': list(question),
    #    'answer': list(answers),
    # }


# class ajaxReturnDataView(View):
#    def get(self, request):
#        thisQuiz = request.GET.get('thisQuiz')
#
#        if request.is_ajax():
#            t = 'n-s-gori'
#            return JsonResponse({'eto': t}, status=200)
#
#        return render(request, 'quiz.html')


def quizResultView(request, quiz):

    if request.POST.get('answers'):
        if (request.POST):
            print('1')
            #post = models.Results.objects.create(
            #   quiz_pk_id=quiz,
            #   dict_answers=''.join(request.POST.get('answers')),
            #   user_id=request.user.id,
            #)
            #post.save()

    questions = models.Questions.objects.filter(quiz_id=quiz)
    results = models.Results.objects.filter(quiz_pk_id=quiz, user_id=request.user.id)

    resultLast = list(results[len(results)-1].dict_answers)
    result = results[len(results)-1]

    answers = []

    lengthAnswers = len(models.Results.objects.filter(quiz_pk_id=quiz)) - 1
    for i in range(lengthAnswers-1):
        print(i)
        answers.append(models.Answers.objects.filter(question_pk=questions[i].id))

    data = {
        'questions': questions,
        'answers': answers,
        'results_dict': resultLast,
    }

    return render(request, "result.html", data)










