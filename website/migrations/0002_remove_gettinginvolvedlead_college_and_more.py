# Generated by Django 4.0.5 on 2022-07-10 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gettinginvolvedlead',
            name='college',
        ),
        migrations.RemoveField(
            model_name='gettinginvolvedlead',
            name='cv',
        ),
        migrations.RemoveField(
            model_name='gettinginvolvedlead',
            name='education',
        ),
        migrations.RemoveField(
            model_name='gettinginvolvedlead',
            name='expectations',
        ),
        migrations.RemoveField(
            model_name='gettinginvolvedlead',
            name='experience',
        ),
    ]