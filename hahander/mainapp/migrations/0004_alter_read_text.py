# Generated by Django 4.1 on 2022-08-15 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='read',
            name='text',
            field=models.TextField(blank=True, max_length=4048, verbose_name='text'),
        ),
    ]
