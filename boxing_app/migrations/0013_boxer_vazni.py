# Generated by Django 4.1.1 on 2022-10-18 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boxing_app', '0012_boxer_nokaut_boxer_qaror_boxer_taqdim_etish_orqali_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='boxer',
            name='vazni',
            field=models.IntegerField(default=0),
        ),
    ]
