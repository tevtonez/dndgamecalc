"""Board game calc views."""

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
    ArmorLootItem,
    GameLog,
    MonsterCharacter,
    PlayerCharacter,
    TrinketLootItem,
    WeaponLootItem,
)


def monster_delete(id):
    """Delete a monster by its ID."""
    try:
        m = MonsterCharacter.objects.get(id=id)
    except:
        m = None

    if m:
        m_race_name = " ".join([str(m), '#' + str(m.name)])
        m.delete()

    return m_race_name


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


def drop_item(attacker, victim):
    """Generate dropped item after a monster/barrel kill."""
    item_type = random.randrange(1, 999)
    item = []

    if item_type <= 350:
        item = WeaponLootItem.objects.filter(item_dropped=False)
    elif 400 < item_type <= 750:
        item = ArmorLootItem.objects.filter(item_dropped=False)
    elif 800 < item_type <= 999:
        item = TrinketLootItem.objects.filter(item_dropped=False)

    if len(item) != 0:
        loot_item = random.choice(item)
        loot_item.item_dropped = True

        # add item to attacker inventory
        if type(loot_item).__name__ == 'WeaponLootItem':
            loot_item.wpn_owned_by = loot_item.wpn_found_by = attacker

        elif type(loot_item).__name__ == 'ArmorLootItem':
            loot_item.arm_owned_by = loot_item.arm_found_by = attacker

        elif type(loot_item).__name__ == 'TrinketLootItem':
            loot_item.trinket_owned_by = loot_item.trinket_found_by = attacker

        loot_item.save()

    else:
        loot_item = "None"

    return loot_item


def add_to_game_log(game_log, msg_to_log):
    """Add msg_to_log string to the top of game_log."""
    game_log.game_log = msg_to_log + game_log.game_log
    game_log.save()


def get_game_log(pk):
    """Take GameLog.pk and return GameLog object."""
    try:
        game_log = GameLog.objects.get(pk=pk)
        return game_log
    except:
        game_log = None
        return redirect('home')


class SignUpView(CreateView):
    """Signup users view."""

    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'main/signup.html'


class IndexView(TemplateView):
    """Main page of calculator."""

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        """get_context_data."""
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

        m_created = monster_create(
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

        # getting game log
        game_log = get_game_log(1)

        if m_created:
            msg_to_log = '<p class="neutral-msg">{} #{} added to the game board.</p>'.format(m_created, m_created.name)
            add_to_game_log(game_log, msg_to_log)

        return redirect('home')


class CombatView(View):
    """Monster Attacks a Player view."""

    def get(self, request, *args, **kwargs):
        """Get method of view."""
        msg_to_log = ''

        # getting combatants
        attacker_id = int(self.kwargs['attacker_id'])
        victim_id = int(self.kwargs['victim_id'])
        monster_hit = self.kwargs['monster_hit']

        # getting game log
        game_log = get_game_log(1)

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
                if victim.character_race != 'bar':
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

                    # generate loot item dropped
                    loot_item_drop = drop_item(attacker, victim)
                    if victim.character_race != 'bar':
                        msg_to_log = '<p class="monster-hit">{} <strong>#{}</strong> dies, dropping loot <i>{}</i></strong></p>'.format(
                            victim,
                            victim.name,
                            loot_item_drop
                        ) + msg_to_log
                    else:
                        msg_to_log = '<p><span class="monster-hit">{} is destroyed!<br>Loot found: <i>{}</i></span><br>{} dealt damage {} {}</p></p><br>'.format(
                            victim,
                            loot_item_drop,
                            attacker,
                            damage_dealt,
                            attack_dices,
                        ) + msg_to_log

        else:
            if monster_hit == '1':
                attacker_display_name = str(attacker) + \
                    " <strong>#" + str(attacker.name) + "</strong>"
            else:
                attacker_display_name = attacker

            msg_to_log = '<p>{} misses...</p>'.format(
                attacker_display_name
            )
        add_to_game_log(game_log, msg_to_log)

        return redirect('home')


class MonsterDeleteView(View):
    """Delete monsters view."""

    def get(self, request, *args, **kwargs):
        """Get method of view."""
        monster_id = self.kwargs['monster_id']

        try:
            m = MonsterCharacter.objects.get(id=monster_id)
        except:
            m = None
            return redirect('home')

        m_deleted = monster_delete(monster_id)

        # getting game log
        game_log = get_game_log(1)

        if m:
            msg_to_log = '<p class="neutral-msg">{} removed from the game board.</p>'.format(m_deleted)
            add_to_game_log(game_log, msg_to_log)

        return redirect('home')


class RespawnPlayer(View):
    """Respawn player."""

    def get(self, request, *args, **kwargs):
        """Process method GET."""
        player_id = self.kwargs['player_id']
        try:
            player = PlayerCharacter.objects.get(id=player_id)
            player.health = player.respawn_health
            player.knocked_down = False
            player.save()

            # getting game log
            game_log = get_game_log(1)

            msg_to_log = '<p class="monster-hit">{} respawned!</p>'.format(player)
            add_to_game_log(game_log, msg_to_log)

        except:
            pass

        return redirect('home')


class ItemDropView(TemplateView):
    """Drop item from user inventory."""

    def get(self, request, *args, **kwargs):
        """Process method GET."""
        player_id = self.kwargs['player_id']
        player = PlayerCharacter.objects.get(id=player_id)
        item_id = self.kwargs['item_id']
        item_class = self.kwargs['item_class']
        game_log = get_game_log(1)

        if item_class == '1':
            try:
                item = WeaponLootItem.objects.get(pk=item_id)
                item.wpn_owned_by = None
                item.item_equipped = False
            except:
                pass

        elif item_class == '2':
            try:
                item = ArmorLootItem.objects.get(pk=item_id)
                item.arm_owned_by = None
                item.item_equipped = False
            except:
                pass

        elif item_class == '3':
            try:
                item = TrinketLootItem.objects.get(pk=item_id)
                item.trinket_owned_by = None
                item.item_equipped = False
            except:
                pass

        item.save()

        # adding event to the logger
        msg_to_log = '<p class="neutral-msg">{} dropped {}</p>'.format(player.name, item)
        add_to_game_log(game_log, msg_to_log)

        return redirect('home')


class ItemEquipView(TemplateView):
    """Drop item from user inventory."""

    def get(self, request, *args, **kwargs):
        """Process method GET."""
        player_id = self.kwargs['player_id']
        player = PlayerCharacter.objects.get(id=player_id)
        item_id = self.kwargs['item_id']
        item_class = self.kwargs['item_class']
        action = self.kwargs['action']
        game_log = get_game_log(1)
        equip_action = 'equipped' if action == '1' else 'put off'

        if item_class == '1':
            try:
                item = WeaponLootItem.objects.get(pk=item_id)
                if action == '1':
                    item.item_equipped = True
                else:
                    item.item_equipped = False

            except:
                pass

        elif item_class == '2':
            try:
                item = ArmorLootItem.objects.get(pk=item_id)
                if action == '1':
                    item.item_equipped = True
                else:
                    item.item_equipped = False
            except:
                pass

        elif item_class == '3':
            try:
                item = TrinketLootItem.objects.get(pk=item_id)
                if action == '1':
                    item.item_equipped = True
                else:
                    item.item_equipped = False
            except:
                pass

        item.save()

        # adding event to the logger
        msg_to_log = '<p class="neutral-msg">{} {} {}</p>'.format(
            player.name,
            equip_action,
            item
        )

        add_to_game_log(game_log, msg_to_log)

        return redirect('home')


class MainIndexView(TemplateView):
    """Nothing special about his view."""

    template_name = 'main/base.html'


# def index(request):
#     HttpResponse("hi there")


##################################################
#                      TODO
##################################################

# 1. dry equip, drop, pass views
# 2. write bonuses calculation funct. for equip, drop, pass

##################################################
##################################################
