from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse



class StudentDashView(TemplateView, LoginRequiredMixin):
    template_name='accounts/studentdash.html'
