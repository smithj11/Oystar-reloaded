from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from oystar.apps.accounts.forms import LoginForm, RegisterForm
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login



class StudentDashView(TemplateView, LoginRequiredMixin):
    template_name='profile.html'

class LoginView(TemplateView):
    template_name='login.html'
    form = LoginForm
    
def register(request):
    if request.method == "POST":
        form= RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(email=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('accounts:profile')
    else:
        form = RegisterForm()
    args = {'form': form}
    return render(request, 'register.html', args)
