# Generated by Django 4.0.4 on 2022-06-08 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=35)),
                ('nickname', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=75)),
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Moodtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagtitle', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Techtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech_title', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('subject', models.CharField(max_length=150)),
                ('body', models.CharField(max_length=8000)),
                ('is_public', models.BooleanField()),
                ('techtag', models.IntegerField()),
                ('moodtag', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_api.developer')),
            ],
        ),
    ]