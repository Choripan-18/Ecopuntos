# Generated by Django 5.1.1 on 2024-11-06 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecopuntosapp', '0002_objects'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='moderator',
            field=models.IntegerField(default=0),
        ),
    ]
