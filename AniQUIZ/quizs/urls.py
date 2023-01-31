from django.urls import path
from . import views

urlpatterns = [
    path('', views.AniquizListView.as_view(), name='home'),
    path('add_quiz', views.quizCreateView, name='add_quiz'),
    path('add_quiz_/<int:pk>', views.quizAdd_questions, name='add_quiz_n'),

]
