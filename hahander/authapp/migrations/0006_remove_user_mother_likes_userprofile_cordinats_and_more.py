# Generated by Django 4.1 on 2022-08-15 09:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_alter_user_activation_key_expires'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='mother_likes',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='cordinats',
            field=models.TextField(blank=True, default=(0, 0), max_length=512, verbose_name='кординаты'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='telegram',
            field=models.TextField(blank=True, default='-', max_length=512, verbose_name='ник'),
        ),
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 17, 9, 9, 42, 711233, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='aboutMe',
            field=models.TextField(blank=True, max_length=512, verbose_name='О маме'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'мертва'), ('W', 'жива')], max_length=1, verbose_name='состояние матери'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tagline',
            field=models.CharField(blank=True, max_length=128, verbose_name='статус'),
        ),
    ]
