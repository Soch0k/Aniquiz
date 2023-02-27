from django.urls import reverse_lazy
from django.views import generic
from . import forms
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import auth




class SignUp(generic.CreateView):
    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    # def log(self, request):
    #     if request.POST["Log"]:
    #         user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
    #         if user:
    #             auth.login(request, user)
    #             return redirect('home')


def RegAndLog (request):
    if request.method == "POST":
        if request.POST.get('Log'):
             user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
             if user:
                 auth.login(request, user)
                 return redirect('home')
        else:
            form = forms.CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                auth.login(request, user)
                return redirect('home')
    return render(request, 'LogAndReg.html')