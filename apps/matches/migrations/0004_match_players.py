# Generated by Django 2.2.4 on 2019-09-28 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_auto_20190908_1431'),
        ('matches', '0003_match_opponent_goals'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='players',
            field=models.ManyToManyField(related_name='matches', to='players.Player', verbose_name='players'),
        ),
    ]