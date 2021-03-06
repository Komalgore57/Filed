# Generated by Django 3.2 on 2021-04-16 16:24

from django.db import migrations, models
import sound.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audiobook',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=100)),
                ('Author', models.CharField(max_length=100)),
                ('Narrator', models.CharField(max_length=100)),
                ('Duration', models.PositiveIntegerField()),
                ('Uploaded', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Duration', models.PositiveIntegerField()),
                ('Uploaded', models.DateField(auto_now_add=True)),
                ('Participants', models.CharField(max_length=1010, validators=[sound.models.check_participants])),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100, unique=True)),
                ('Duration', models.PositiveIntegerField()),
                ('Uploaded', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
