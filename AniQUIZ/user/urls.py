from django.urls import path
from . import views

urlpatterns = [
    path('authentication/', views.RegAndLog, name='authentication'),
    path('personal_account/<int:pk>', views.personalAccountView.as_view(), name='personal_account'),
]