# Generated by Django 2.0.3 on 2018-03-25 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20180325_2157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weaponlootitem',
            name='wpn_equipped_by',
        ),
        migrations.RemoveField(
            model_name='weaponlootitem',
            name='wpn_found_by',
        ),
    ]