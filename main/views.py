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


def monster_create(
    x_times,
    name,
    character_race,
    health,
    armor,
    character_description,
    attack_range=0,
    attack_modifier=0,
    speed=0,
    character_level=1,
    attack=3,
):
    """Create monster."""
    for i in range(x_times):

        if character_race == 'bar':
            name = len(MonsterCharacter.objects.filter().filter(character_race='bar')) + 1

        m = MonsterCharacter(
            name=name,
            character_race=character_race,
            health=health,
            armor=armor,
            character_description=character_description,
            attack_range=attack_range,
            speed=speed,
            character_level=character_level,
            attack=attack,
        )
        m.save()

    return m


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

        # creating 3 barrels
        if monster_race == "bar":
            x_times = 3
            name = 1
            race = monster_race
            health = 1
            armor = 8
            attack_range = 0
            attack_modifier = 0
            speed = 0
            character_level = 1
            attack = 0
            character_description = "An ordinary barrel people to use to store their stuff in. This one is full of cobwebs and maybe some goods, you never know until you check..."

        monster_create(
            x_times,
            name,
            race,
            health,
            armor,
            character_description,
            attack_range=attack_range,
            attack_modifier=attack_modifier,
            speed=speed,
            character_level=character_level,
            attack=attack
        )

        return redirect('home')


class MainIndexView(TemplateView):
    """Nothing special about his view."""

    template_name = 'main/base.html'


# def index(request):
#     HttpResponse("hi there")
