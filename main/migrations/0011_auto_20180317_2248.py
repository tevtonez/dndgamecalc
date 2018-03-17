# Generated by Django 2.0.3 on 2018-03-17 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20180317_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armorlootitem',
            name='modificator_negative',
            field=models.CharField(choices=[('na', 'na'), ('-1', '-1'), ('-2', '-2'), ('-3', '-3'), ('-4', '-4')], default='-1', max_length=2),
        ),
        migrations.AlterField(
            model_name='armorlootitem',
            name='modificator_positive',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=1),
        ),
    ]
