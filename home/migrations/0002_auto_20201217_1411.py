# Generated by Django 3.0.8 on 2020-12-17 14:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='note',
        ),
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2020, 12, 17)),
        ),
    ]
