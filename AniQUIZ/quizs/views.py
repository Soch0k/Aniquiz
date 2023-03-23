from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import generic, View
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms, models


import json


def AniquizListView(request):
    model = models.Quiz.objects.all()

    RatingForSorted = {}

    for rating_pk in model:
        marks = rating_pk.rating.split()
        try:
            RatingForSorted[rating_pk.pk] = (round(int(marks[0]) / int(marks[1]), 2))
        except:
            RatingForSorted[rating_pk.pk] = (0)

    sortRating = sorted(RatingForSorted.items(), key=lambda x:x[1], reverse=True)
    converted_sortRating = dict(sortRating)

    model_sorted = []
    for key in converted_sortRating:
        model_sorted.append(models.Quiz.objects.filter(pk=key))

    rating = []
    for i in model_sorted:
        for Rating in i:
            marks = Rating.rating.split()
            try:
                rating.append(round(int(marks[0]) / int(marks[1]), 2))
            except:
                rating.append(0)

    ModelAndRating = dict(pairs=zip(model_sorted, rating))

    data = {
        "ModelAndRating": ModelAndRating,
    }

    return render(request, "home.html", data)

def quizCreateView(request):
    if request.user.pk:
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
    else:
        return redirect('authentication')


def quizAdd_questions(request, pk):
    if request.user.pk:
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


        questions = models.Questions.objects.filter(quiz=pk)
        ansswers = []
        for i in questions:
            ansswers.append(models.Answers.objects.filter(question_pk=i.pk))

        quiestionsAndAnswers = dict(pairs=zip(questions, ansswers))

        data = {
            'quiestionsAndAnswers': quiestionsAndAnswers,
            'form': form,
            'errors': errors,
            'quiz_pk': pk,
            'nav': 'addquiz',
        }
        return render(request, 'add_quiz.html', data)
    else:
        return redirect('authentication')


def quizAdd_answers(request, pk):

    errors = {}

    if request.user.pk:
        if request.method == 'POST':
            print(request.POST)
            print(len(request.POST))

            req = request.POST

            for key in request.POST:
                if key[:-1] == 'answer':
                    try:
                        if key == req['correct']:
                            post = models.Answers.objects.create(
                                answer=req[key],
                                question_pk_id=pk,
                                correct=1,
                            )
                            post.save()
                    except:
                        errors = {
                            'pk_question': pk,
                            'nav': 'addquiz',
                            'errors': 'в форме есть ошибки, она не заполнена или не указан верный ответ'
                        }
                        return render(request, 'add_answers.html', errors)

                    else:
                        try:
                            if key != req['correct']:
                                post = models.Answers.objects.create(
                                    answer=req[key],
                                    question_pk_id=pk,
                                    correct=0,
                                )
                                post.save()
                        except:
                            errors = {
                                'pk_question': pk,
                                'nav': 'addquiz',
                                'errors': 'в форме есть ошибки, она не заполнена или не указан верный ответ'
                            }
                            return render(request, 'add_answers.html', errors)

            # pk_qst =
            return redirect('add_quiz_n', models.Questions.objects.filter(id=pk)[0].quiz_id)
        data = {
            'pk_question': pk,
            'nav': 'addquiz',
        }
        return render(request, 'add_answers.html', data)
    else:
        return redirect('authentication')


def addQuestion(request):
    if request.user.pk:
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
    else:
        return redirect('authentication')


def quizView(request, pk):
    if request.user:
        form = models.Quiz.objects.filter(pk=pk)
        questions = models.Questions.objects.filter(quiz=form[0].pk)

        quiz = models.Quiz.objects.get(pk=pk)


        marks = quiz.rating.split()
        try:
            rating = round(int(marks[0]) / int(marks[1]), 2)
        except:
            rating = 0

        answers = models.Answers
        data = {
            'pkQuiz': pk,
            'quiz': form,
            'questions': questions,
            'answers': answers,
            'nav': 'quiz',
            'result': rating,
        }

        return render(request, 'quiz.html', data)
    else:
        return redirect('authentication')


def returnThisQuestion(request, quiz, num):
    try:
        Question = list(models.Questions.objects.values('question', 'image', 'quiz').filter(quiz=quiz))[int(num)]
        takePkQuestionForAnswers = models.Questions.objects.filter(quiz=quiz)
        answers = list(models.Answers.objects.values('id', 'answer', 'correct', 'question_pk').filter(question_pk=((takePkQuestionForAnswers[num]).pk)))

        return JsonResponse({'Question': Question, 'Answers': answers})
    except:
        return JsonResponse()


def quizResultView(request, quiz):
    if request.user.pk:
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
    else:
        return redirect('authentication')

def AllResultsView(request):
    if request.user.pk:
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
    else:
        return redirect('authentication')

def questionRedactView(request, pk):
    question = models.Questions.objects.filter(pk=pk)
    answers = models.Answers.objects.filter(question_pk_id=question[0].pk)
    form = forms.QuestionRedactForm


    if request.method == 'POST':
        if request.POST.get('question'):
            models.Questions.objects.filter(pk=pk).update(question=request.POST.get('question'))
            if request.FILES:
                her = 'static/img/quizs_img/questions_img/' + request.FILES['image']._get_name()
                models.Questions.objects.filter(pk=pk).update(image=her)
        if request.POST.get('idAnswer'):
            models.Answers.objects.filter(pk=request.POST['idAnswer']).update(answer=request.POST['answer'])




    data = {
        'question': question[0],
        'answers': answers,
        'formQuestion': form,
        'nav': 'addquiz',
    }

    return render(request, 'redact/editQuestion.html', data)

#def answersRedactView(request, pkQue, pkAns):
#    question = models.Questions.objects.filter(pk=pkQue)
#    answers = models.Answers.objects.filter(question_pk_id=question[0].pk)
#
#    if request.POST:
#
#
#
#    data = {
#        'question': question[0],
#        'formQuestion': form,
#    }
#
#    return render(request, 'redact/editQuestion.html', data)

def QuizsAndRating(request):
    quiz = models.Quiz.objects.all()

    rating = []

    for rating_pk in quiz:
        marks = rating_pk.rating.split()
        try:
            rating.append(round(int(marks[0]) / int(marks[1]), 2))
        except:
            rating.append(0)

    QuizsAndRating = dict(pairs=zip(quiz, rating))

    data = {
        'QuizsAndRating': QuizsAndRating,
    }


def quizAllView(request):
    model = models.Quiz.objects.all()

    rating = {}

    for rating_pk in model:
        marks = rating_pk.rating.split()
        try:
            rating[rating_pk.pk] = (round(int(marks[0]) / int(marks[1]), 2))
        except:
            rating[rating_pk.pk] = (0)

    ratingList = []

    for key in rating:
        ratingList.append(rating[key])

    
    QuizAndRating = dict(pairs=zip(model, ratingList))

    data = {
        'QuizAndRating': QuizAndRating,
        'nav': 'quiz',
    }

    return render(request, 'all_quiz.html', data)

class deleteQuizView(DeleteView, LoginRequiredMixin):
    model = models.Quiz
    template_name = 'redact/delete.html'
    success_url = reverse_lazy('home')
    login_url = 'authentication'


def deleteQuestionView(request, pk):
    if request.user:
        if request.method == 'POST':
            model = models.Questions.objects.get(pk=pk)
            model.delete()
            return redirect('add_quiz_n', pk)
    else:
        return redirect('authentication')

    return render(request,)
    

def SuplyQuizView(request, pk):
    if request.POST:
        if request.user.is_superuser:
            if request.POST.get('suply'):
                models.Quiz.objects.filter(pk=pk).update(status=True)
                return redirect('checking_quizs')
        else:
            return redirect('Не достаточно прав')
    else:
        data = {
            'status': True,
            'quiz': pk,
        }
        return render(request, 'result.html', data)


def CheckingQuizView(request):
    model = models.Quiz.objects.filter(status=0)

    rating = {}

    for rating_pk in model:
        marks = rating_pk.rating.split()
        try:
            rating[rating_pk.pk] = (round(int(marks[0]) / int(marks[1]), 2))
        except:
            rating[rating_pk.pk] = (0)

    ratingList = []

    for key in rating:
        ratingList.append(rating[key])

    
    QuizAndRating = dict(pairs=zip(model, ratingList))

    data = {
        'QuizAndRating': QuizAndRating,
        'nav': 'addquiz',
        'admin': True
    }

    return render(request, 'all_quiz.html', data)




# class deleteQuestionView(DeleteView, LoginRequiredMixin):
#     model = models.Questions
#     template_name = 'redact/delete.html'
#     success_url = reverse_lazy('home')
#     login_url = 'login'