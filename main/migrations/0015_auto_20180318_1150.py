# Generated by Django 2.0.3 on 2018-03-18 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20180318_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armorlootitem',
            name='modificator_negative',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default='-1', max_length=2),
        ),
    ]
