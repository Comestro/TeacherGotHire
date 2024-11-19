# Generated by Django 5.1.3 on 2024-11-18 09:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacherhire', '0012_level_subject_id_qualification_user_id_skill_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='qualification',
            old_name='institution',
            new_name='institute',
        ),
        migrations.RenameField(
            model_name='qualification',
            old_name='highest_qualification',
            new_name='qualification_name',
        ),
        migrations.RemoveField(
            model_name='qualification',
            name='board',
        ),
        migrations.RemoveField(
            model_name='qualification',
            name='skill_name',
        ),
        migrations.AddField(
            model_name='qualification',
            name='percentage',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
        model_name='qualification',
        name='user_id',
        field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
    ),
]