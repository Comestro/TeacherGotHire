# Generated by Django 5.1.3 on 2024-11-16 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacherhire', '0004_alter_qualification_board_alter_rating_rating_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=500)),
                ('Lname', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=200)),
                ('contact', models.IntegerField()),
            ],
        ),
    ]
