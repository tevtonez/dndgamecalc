# Generated by Django 2.0.3 on 2018-03-25 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20180325_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamelog',
            name='game_log',
            field=models.TextField(default='<p>Game log start.</p>'),
        ),
    ]
