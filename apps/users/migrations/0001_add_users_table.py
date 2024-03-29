# Generated by Django 4.2 on 2024-02-15 02:41

import apps.users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('is_admin', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'users',
            },
            managers=[
                ('objects', apps.users.models.UserManager()),
            ],
        ),
    ]
