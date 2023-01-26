from django.urls import reverse_lazy
from django.views import generic
from . import forms


class SignUp(generic.CreateView):
    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
