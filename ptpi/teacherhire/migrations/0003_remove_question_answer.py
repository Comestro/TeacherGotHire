# Generated by Django 5.1.3 on 2024-11-21 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacherhire', '0002_delete_adminlogin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
    ]