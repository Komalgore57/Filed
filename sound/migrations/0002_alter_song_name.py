# Generated by Django 3.2 on 2021-04-16 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sound', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='Name',
            field=models.CharField(max_length=100),
        ),
    ]
