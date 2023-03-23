from django.urls import path
from . import views

urlpatterns = [
    path('', views.AniquizListView, name='home'),
    path('add_quiz', views.quizCreateView, name='add_quiz'),
    path('add_quiz/<int:pk>', views.quizAdd_questions, name='add_quiz_n'),
    path('add_quiz_answers/<int:pk>', views.quizAdd_answers, name='add_quiz_answers'),
    path('quiz/<int:pk>', views.quizView, name='quiz'),
    path('quiz/<int:quiz>/<int:num>', views.returnThisQuestion, name='jquery'),
    path('quiz/result/<int:quiz>', views.quizResultView, name='result'),
    path('user/All-results', views.AllResultsView, name='allResults'),
    path('quiz/question/redact/<int:pk>', views.questionRedactView, name='redact_question'),
    path('quiz/watch-all', views.quizAllView, name='quiz_all'),
    path('quiz/delete/<int:pk>', views.deleteQuizView.as_view(), name='delete_quiz'),
    path('quiz/question/delete/<int:pk>', views.deleteQuestionView, name='delete_question'),
    path('quiz/suply/<int:pk>', views.SuplyQuizView, name='suply_quiz'),
    path('quiz/check/', views.CheckingQuizView, name='checking_quizs'),

]
