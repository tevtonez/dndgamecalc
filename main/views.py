from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.decorators import login_required

from . import forms
from . import models

class SignUpView(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'main/signup.html'


class IndexView(TemplateView):
    template_name = 'index.html'


class mainIndexView(TemplateView):
    template_name = 'main/base.html'


# def index(request):
#     HttpResponse("hi there")
