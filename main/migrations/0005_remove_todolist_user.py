# Generated by Django 4.2.19 on 2025-02-07 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_todolist_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='user',
        ),
    ]
