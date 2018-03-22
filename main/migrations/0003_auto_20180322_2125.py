# Generated by Django 2.0.3 on 2018-03-22 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180322_2113'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerCharacter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('health', models.IntegerField(default=4)),
                ('armor', models.IntegerField(default=5)),
                ('attack', models.IntegerField(default=3)),
                ('attack_range', models.IntegerField(default=0)),
                ('attack_modifier', models.IntegerField(default=0)),
                ('speed', models.IntegerField(default=5)),
                ('character_level', models.IntegerField(default=1)),
                ('character_description', models.TextField(default='Character description...', max_length=1500)),
                ('player', models.BooleanField(default=True)),
                ('character_race', models.CharField(choices=[('hum', 'Human'), ('dwa', 'Dwarf'), ('elf', 'Elf')], default='hum', max_length=3)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='GamerCharacter',
        ),
    ]
