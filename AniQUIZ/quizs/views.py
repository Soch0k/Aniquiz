from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import generic, View
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from . import forms, models
from . import models as Models
import json


# class AniquizListView(ListView):
#     model = models.Quiz
#     template_name = "home.html"
#
#     extra_context = {'mark': 'Главная страница'}

def AniquizListView(request):
    model = models.Quiz.objects.all()
    rating = []
    for Rating in model:
        marks = Rating.rating.split()
        try:
            rating.append(round(int(marks[0]) / int(marks[1]), 2))
        except:
            rating.append(0)

    ModelAndRating = dict(pairs=zip(model, rating))

    data = {
        "ModelAndRating": ModelAndRating,
    }

    return render(request, "home.html", data)

def quizCreateView(request):
    errors = ''
    category = models.cateory.objects.all()
    if request.method == 'POST':
        form = forms.QuizForm(request.POST, request.FILES)

        if form.is_valid():
            model = models.Quiz(
                title=request.POST.get('title'),
                description=request.POST.get('description'),
                imageScreensaver=request.FILES.get('imageScreensaver'),
                category_id=request.POST.get('category'),
                user_id=request.user.id,
            )

            model.save()
            return redirect('add_quiz_n', pk=model.pk)
        else:
            errors = form.errors

    data = {
        'errors': errors,
        'category': category,
        'nav': 'addquiz',
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
        'nav': 'addquiz',
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
        return redirect('add_quiz_n', models.Questions.objects.filter(id=pk)[0].quiz_id)
    data = {
        'pk_question': pk,
        'nav': 'addquiz',
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
        'nav': 'addquiz',
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
        'nav': 'quiz',
    }

    return render(request, 'quiz.html', data)


def returnThisQuestion(request, quiz, num):
    try:
        Question = list(models.Questions.objects.values('question', 'image', 'quiz').filter(quiz=quiz))[int(num)]
        takePkQuestionForAnswers = models.Questions.objects.filter(quiz=quiz)
        answers = list(models.Answers.objects.values('id', 'answer', 'correct', 'question_pk').filter(
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
        if models.Results.objects.filter(quiz_pk_id=quiz, user_id=request.user.id):
            models.Results.objects.filter(quiz_pk_id=quiz, user_id=request.user.id).update(dict_answers=''.join(request.POST.get('answers')))
        else:
            if (request.POST):
                post = models.Results.objects.create(
                   quiz_pk_id=quiz,
                   dict_answers=''.join(request.POST.get('answers')),
                   user_id=request.user.id,
                )
                post.save()
                popular = models.Quiz.objects.get(id=quiz)
                models.Quiz.objects.filter(id=quiz).update(popular=popular.popular+1)

    if request.POST.get('ThisRating'):
        rating = models.Quiz.objects.get(id=quiz).rating
        ratingList = rating.split()
        ratingStatus = models.RatingStatus.objects.filter(quiz_id=quiz, user=request.user.id)

        if ratingStatus:
            ratingList[0] = int(ratingList[0]) - int(ratingStatus[0].mark) + int(request.POST.get('rating'))
            ratingStatus.update(mark=int(request.POST.get('rating')))
            models.Quiz.objects.filter(id=quiz).update(rating=' '.join(str(x) for x in ratingList))
        else:
            ratingList[0] = int(ratingList[0]) + int(request.POST.get('rating'))
            ratingList[1] = int(ratingList[1]) + 1
            models.Quiz.objects.filter(id=quiz).update(rating=' '.join(str(x) for x in ratingList))
            models.RatingStatus.objects.create(
                user_id=request.user.id,
                quiz_id=quiz,
                mark=int(request.POST.get('rating'))
            )

    questions = models.Questions.objects.filter(quiz_id=quiz)
    results = models.Results.objects.get(quiz_pk_id=quiz, user_id=request.user.id).dict_answers

    resultLast = results.split()
    answers = []

    #lengthAnswers = len(models.Results.objects.filter(quiz_pk_id=quiz)) - 1
    for i in range(len(resultLast)):
        answers.append(models.Answers.objects.filter(question_pk_id=questions[i].id))

    ansersAndResulstAndQuestions = dict(pairs=zip(answers, resultLast, questions))

    ratingStatus = models.RatingStatus.objects.filter(quiz_id=quiz, user=request.user.id)

    data = {
        'ansersAndResulstAndQuestions': ansersAndResulstAndQuestions,
        'ratingStatus': ratingStatus,
        'nav': 'res',
    }

    return render(request, "result.html", data)

def AllResultsView(request):
    result = models.Results.objects.filter(user_id=request.user.id)
    quizs = []
    for i in range(len(result)):
        quizs.append(models.Quiz.objects.filter(id=result[i].quiz_pk_id))

    rating = []
    for Rating in quizs:
        for Ra in Rating:
            marks = Ra.rating.split()
            try:
                rating.append(round(int(marks[0]) / int(marks[1]), 2))
            except:
                rating.append(0)

    ModelAndRating = dict(pairs=zip(quizs, rating))

    data = {
        'ModelAndRating': ModelAndRating,
        'nav': 'res',
    }

    return render(request, 'all_results.html', data)









