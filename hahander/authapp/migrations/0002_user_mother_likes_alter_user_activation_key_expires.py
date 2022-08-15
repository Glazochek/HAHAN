# Generated by Django 4.1 on 2022-08-15 06:33

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mother_likes',
            field=models.CharField(default=django.utils.timezone.now, max_length=64, unique=True, verbose_name='имя'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 17, 6, 33, 28, 116413, tzinfo=datetime.timezone.utc)),
        ),
    ]