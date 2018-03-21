from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.decorators import login_required

from main import forms
from main.models import (
    GamerCharacter,
    MonsterCharacter,
)

class SignUpView(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'main/signup.html'


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        duke = GamerCharacter.objects.get(name='Duke Vincent')
        dadrin = GamerCharacter.objects.get(name='Dadrin')
        idrill = GamerCharacter.objects.get(name='Idrill')

        context['players'] = [duke, dadrin, idrill]
        context['monsters'] = MonsterCharacter.objects.all()

        return context



class mainIndexView(TemplateView):
    template_name = 'main/base.html'


# def index(request):
#     HttpResponse("hi there")
