# Generated by Django 4.1.1 on 2022-09-14 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boxing_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boxer',
            name='trener_1',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AddField(
            model_name='boxer',
            name='trener_2',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AddField(
            model_name='boxer',
            name='trener_3',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AddField(
            model_name='boxer',
            name='trener_4',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AddField(
            model_name='boxer',
            name='trener_5',
            field=models.CharField(default='None', max_length=200),
        ),
    ]
