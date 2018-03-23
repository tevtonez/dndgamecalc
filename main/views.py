from django.shortcuts import (
    # render,
    redirect,
    # get_object_or_404
)
# from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    TemplateView,
    View,
    # ListView,
    # DetailView,
    # UpdateView,
    # DeleteView
)
# from django.contrib.auth.decorators import login_required
from main import forms

from main.models import (
    MonsterCharacter,
    PlayerCharacter,
)


class SignUpView(CreateView):
    """Signup users view."""

    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'main/signup.html'


class IndexView(TemplateView):
    """Main page of calculator."""

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        duke = PlayerCharacter.objects.get(name='Duke Vincent')
        dadrin = PlayerCharacter.objects.get(name='Dadrin')
        idrill = PlayerCharacter.objects.get(name='Idrill')

        context['players'] = [duke, dadrin, idrill]
        context['monsters'] = MonsterCharacter.objects.all()

        return context


class MonsterCreateView(View):
    """Crete monsters"""

    def get(self, request, *args, **kwargs):
        """Get HTTP method."""
        monster_race = self.kwargs['monster_race']
        monster_name = self.kwargs['monster_number']

        # creting barrel

        return redirect('home')


class MainIndexView(TemplateView):
    """Nothing special about his view."""

    template_name = 'main/base.html'


# def index(request):
#     HttpResponse("hi there")
