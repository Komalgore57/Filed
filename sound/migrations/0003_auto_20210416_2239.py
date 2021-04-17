# Generated by Django 3.2 on 2021-04-16 17:09

from django.db import migrations, models
import sound.models


class Migration(migrations.Migration):

    dependencies = [
        ('sound', '0002_alter_song_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiobook',
            name='Uploaded',
            field=models.DateField(validators=[sound.models.check_time]),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='Uploaded',
            field=models.DateField(validators=[sound.models.check_time]),
        ),
        migrations.AlterField(
            model_name='song',
            name='Uploaded',
            field=models.DateField(validators=[sound.models.check_time]),
        ),
    ]
