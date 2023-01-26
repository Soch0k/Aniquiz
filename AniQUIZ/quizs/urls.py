from django.urls import path
from . import views

urlpatterns = [
    path('', views.AniquizListView.as_view(), name='home'),

]
