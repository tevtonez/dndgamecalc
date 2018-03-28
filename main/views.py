import random

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

# from main.helpers.common import find_value

from main.models import (
    GameLog,
    MonsterCharacter,
    PlayerCharacter,
)


def monster_delete(id):
    """Delete a monster by its ID."""
    try:
        m = MonsterCharacter.objects.get(id=id)
    except:
        m = None

    if m:
        m.delete()


def monster_create(
    x_times,
    name,
    character_race,
    health,
    armor,
    character_description,
    monster,
    attack_range=0,
    attack_modifier=0,
    speed=0,
    character_level=1,
    attack=3,
):
    """Create monster."""
    for i in range(x_times):

        m = MonsterCharacter(
            name=name,
            character_race=character_race,
            health=health,
            armor=armor,
            character_description=character_description,
            attack_range=attack_range,
            attack_modifier=attack_modifier,
            speed=speed,
            character_level=character_level,
            attack=attack,
            monster=monster,
        )
        m.save()

    return m


def calculate_damage(dices):
    """Calculate dealt damage."""
    resulting_damage = 0
    dices_dealt = []

    for _ in range(dices):
        dice_damage = random.randint(1, 6)
        resulting_damage += dice_damage
        dices_dealt.append(dice_damage)

    return resulting_damage, dices_dealt


def victim_dies(victim):
    """Check if attacked player/creature has enough of health."""
    if victim.health >= 2:
        victim.health -= 1
        victim.save()
        return False

    elif victim.health == 1:
        return True


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

        # getting players
        try:
            duke = PlayerCharacter.objects.get(name='Vincent')
            dadrin = PlayerCharacter.objects.get(name='Dadrin')
            idrill = PlayerCharacter.objects.get(name='Idrill')
        except:
            context['players'] = None
            return context

        # getting monsters
        monsters_list = MonsterCharacter.objects.all().order_by('-id')

        # getting log
        try:
            game_log = GameLog.objects.get(pk=1)
        except:
            game_log = None

        context['players'] = [duke, dadrin, idrill]
        context['game_log'] = game_log
        context['monsters'] = monsters_list
        context['monsters_count'] = len(monsters_list.filter(monster=True))
        context['objects_count'] = len(monsters_list.filter(monster=False))

        return context


class MonsterCreateView(View):
    """Create monsters."""

    def get(self, request, *args, **kwargs):
        """Get HTTP method."""
        monster_race = self.kwargs['monster_race']
        monster_name = self.kwargs['monster_number']

        # creating 3 barrels

        if monster_race == "bar":
            x_times = 3
            name = ''
            race = monster_race
            health = 1
            armor = 8
            attack_range = 0
            attack_modifier = 0
            speed = 0
            character_level = 1
            attack = 0
            monster = False
            character_description = "An ordinary barrel people to use to store their stuff in.\nThis one is full of cobwebs and maybe some goods, you never know until you check..."

        # creating Skeleton lev.1
        elif monster_race == "ske1":
            x_times = 1
            name = monster_name
            race = 'ske'
            character_level = 1
            health = 4
            armor = 8
            speed = 4
            attack = 3
            attack_range = 1
            attack_modifier = 0
            monster = True
            character_description = "A walking skeleton, with some withered flesh on its bones.\nThe very appearance of this creation infuses an endless paralyzing horror in everyone who sees it. The chilling look of the empty eye sockets of the skeleton penetrates right into the soul, emptying it and depleting the strength of living beings."

        # creating Skeleton lev.2
        elif monster_race == "ske2":
            x_times = 1
            name = monster_name
            race = 'ske'
            character_level = 2
            health = 6
            armor = 10
            speed = 5
            attack = 3  # 3d6
            attack_range = 1
            attack_modifier = 0
            monster = True
            character_description = "A walking skeleton, with a rusty chipped sword with huge nicks here and there on its blade.\nThis fast and fierce monster inhabits the darkest levels of Skeleton cave where it has the most of the advantage by attacking adventurers from the dark."

        # creating Archer Skeleton lev.2
        elif monster_race == "ska":
            x_times = 1
            name = monster_name
            race = monster_race
            character_level = 2
            health = 5
            armor = 8
            speed = 5
            attack = 3  # 3d6
            attack_range = 5
            attack_modifier = 0
            monster = True
            character_description = "A walking skeleton, with a strong bow.\nThis silent monster kills quickly with precise shots. Its victims never know what killed them."

        # creating Spider lev.1
        elif monster_race == "spd":
            x_times = 1
            name = monster_name
            race = monster_race
            character_level = 1
            health = 2
            armor = 8
            speed = 2
            attack = 2  # 2d6
            attack_range = 1
            attack_modifier = 0
            monster = True
            character_description = "A shiny black fat spider with hairy paws.\nHis black, shining eyes are staring at you, and fluorescing in the dark poison is dripping from its fangs."

        # creating Flying Spinner - the Boss
        elif monster_race == "fsp":
            x_times = 1
            name = ''
            race = monster_race
            character_level = 1
            health = 10
            armor = 14
            speed = 6
            attack = 3  # 3d6
            attack_range = 1
            attack_modifier = 1
            monster = True
            character_description = "Run, you fulls!!!"

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
            attack=attack,
            monster=monster
        )

        return redirect('home')


class CombatView(View):
    """Monster Attacks a Player view."""

    def get(self, request, *args, **kwargs):
        msg_to_log = ''

        # getting combatants
        attacker_id = int(self.kwargs['attacker_id'])
        victim_id = int(self.kwargs['victim_id'])
        monster_hit = self.kwargs['monster_hit']

        # getting game log
        try:
            game_log = GameLog.objects.get(pk=1)
        except:
            game_log = None
            return redirect('home')

        if monster_hit == '1':
            attacker = MonsterCharacter.objects.get(id=attacker_id)
            victim = PlayerCharacter.objects.get(id=victim_id)
        else:
            attacker = PlayerCharacter.objects.get(id=attacker_id)
            victim = MonsterCharacter.objects.get(id=victim_id)

        attack_dices = attacker.attack

        # getting damage value and dices' numbers
        damage = calculate_damage(attack_dices)
        damage_dealt = damage[0] + attacker.attack_modifier
        attack_dices = damage[1]

        # validating attack success
        if damage_dealt >= victim.armor:

            if monster_hit == '1':
                msg_to_log = '<p><span class="hero-hit">{3} looses 1HP!</span><br>{0} #{1} dealt damage {2} {4}</p>'.format(
                    # find_value(attacker.RACE, attacker.character_race),
                    attacker,
                    attacker.name,
                    damage_dealt,
                    victim,
                    attack_dices,
                )
                dies = victim_dies(victim)
                if dies:
                    victim.knocked_down = True
                    victim.save()
                    msg_to_log += '<p class="hero-hit">{} knocked down! Respawn in camp in 2 rounds.</p><br>'.format(victim)

            else:
                msg_to_log = '<p><span class="monster-hit">{0} <strong>#{1}</strong> looses 1HP!</span><br>{2} dealt damage {3} {4}</p>'.format(
                    # find_value(attacker.RACE, attacker.character_race),
                    victim,
                    victim.name,
                    attacker,
                    damage_dealt,
                    attack_dices,
                )
                # checking victim's previous health
                dies = victim_dies(victim)
                if dies:
                    victim.delete()
                    msg_to_log += '<p class="monster-hit">{} <strong>#{}</strong> dies!</p><br>'.format(
                        victim,
                        victim.name
                    )

        else:
            if monster_hit == '1':
                attacker_display_name = str(attacker) + \
                    " <strong>#" + str(attacker.name) + "</strong>"
            else:
                attacker_display_name = attacker

            msg_to_log = '<p>{} misses...</p>'.format(
                attacker_display_name
            )
        game_log.game_log = msg_to_log + game_log.game_log

        game_log.save()

        return redirect('home')


class MonsterDeleteView(View):
    """Delete monsters view."""

    def get(self, request, *args, **kwargs):
        monster_id = self.kwargs['monster_id']

        monster_delete(monster_id)

        return redirect('home')


class RespawnPlayer(View):
    """Respawn player."""

    def get(self, request, *args, **kwargs):
        player_id = self.kwargs['player_id']
        try:
            player = PlayerCharacter.objects.get(id=player_id)
            player.health = player.respawn_health
            player.knocked_down = False
            player.save()

            # getting game log
            try:
                game_log = GameLog.objects.get(pk=1)
            except:
                game_log = None
                return redirect('home')

            msg_to_log = '<p class="monster-hit">{} respawned!</p>'.format(player)
            game_log.game_log = msg_to_log + game_log.game_log
            game_log.save()

        except:
            return redirect('home')

        return redirect('home')


class MainIndexView(TemplateView):
    """Nothing special about his view."""

    template_name = 'main/base.html'


# def index(request):
#     HttpResponse("hi there")
