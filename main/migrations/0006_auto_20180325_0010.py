# Generated by Django 2.0.3 on 2018-03-25 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_playercharacter_knocked_down'),
    ]

    operations = [
        migrations.AddField(
            model_name='monstercharacter',
            name='respawn_health',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='playercharacter',
            name='respawn_health',
            field=models.IntegerField(default=4),
        ),
    ]
