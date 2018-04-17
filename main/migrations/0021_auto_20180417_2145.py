# Generated by Django 2.0.3 on 2018-04-17 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20180417_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armorlootitem',
            name='item_type',
            field=models.CharField(choices=[('wpn', 'weapon'), ('arm', 'armor'), ('trn', 'trinket')], default='arm', max_length=3),
        ),
        migrations.AlterField(
            model_name='trinketlootitem',
            name='item_type',
            field=models.CharField(choices=[('wpn', 'weapon'), ('arm', 'armor'), ('trn', 'trinket')], default='arm', max_length=3),
        ),
        migrations.AlterField(
            model_name='weaponlootitem',
            name='item_type',
            field=models.CharField(choices=[('wpn', 'weapon'), ('arm', 'armor'), ('trn', 'trinket')], default='arm', max_length=3),
        ),
    ]
