# Generated by Django 3.0.8 on 2020-12-16 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yard', '0002_auto_20201210_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='time',
            field=models.CharField(choices=[('5:00', '5:00'), ('6:00', '6:00'), ('7:00', '7:00'), ('8:00', '8:00'), ('9:00', '9:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'), ('21:00', '21:00'), ('22:00', '22:00')], max_length=255, unique=True),
        ),
    ]
