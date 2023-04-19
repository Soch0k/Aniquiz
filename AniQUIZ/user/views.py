from django.urls import reverse_lazy
from django.views import generic
from . import forms, models
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView
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
    data = {}

    if request.method == "POST":
        if request.POST.get('Log'):
             user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
             if user:
                 auth.login(request, user)
                 return redirect('home')
             else:
                 data = {
                     'usernameLog': request.POST.get('username'),
                     'errors': 'errors'
                 }

        else:
            form = forms.CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                auth.login(request, user)
                return redirect('home')
            else:
                data = {
                    'username': request.POST.get('username'),
                    'email': request.POST.get('email'),
                    'errors': 'errors'
                }

    return render(request, 'LogAndReg.html', data)


# def personalAccountView(request, pk):
#
#     if request.method == "POST":
#         if request.FILES['icon']:
#             form = forms.UserChangeIconForm(request.FILES, instance=request.user)
#
#             if form.is_valid():
#                 icon = request.FILES
#                 print(icon)
#                 print(form)
#                 models.CustomUser.objects.filter(pk=pk).update(icon=request.FILES['icon'])
#
#
#             # model = models.CustomUser.objects.get(pk=pk)
#             # model.icon = request.FILES
#             # model.save()
#         #print('huilaebuchii')
#         #models.CustomUser.objects.filter(pk=pk).update(icon=request.FILES)
#         #model.save()
#
#
#     data = {
#         'userIn': models.CustomUser.objects.filter(pk=pk)
#     }
#
#     return render(request, 'personal_account.html', data)


class personalAccountView(UpdateView):
    model = models.CustomUser
    fields = ['username', 'icon']
    template_name = 'personal_account.html'
    success_url = reverse_lazy('home')