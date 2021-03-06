# Generated by Django 2.0.3 on 2018-03-25 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20180325_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='armorlootitem',
            name='equiped_on',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.PlayerCharacter'),
        ),
        migrations.AddField(
            model_name='trinketlootitem',
            name='equiped_on',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.PlayerCharacter'),
        ),
        migrations.AddField(
            model_name='weaponlootitem',
            name='equiped_on',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.PlayerCharacter'),
        ),
    ]
