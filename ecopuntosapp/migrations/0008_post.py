# Generated by Django 5.1.1 on 2024-12-04 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecopuntosapp', '0007_useraccounts_delete_accounts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
