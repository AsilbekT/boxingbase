# Generated by Django 4.1.1 on 2022-10-18 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boxing_app', '0013_boxer_vazni'),
    ]

    operations = [
        migrations.CreateModel(
            name='Different_weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight_start', models.IntegerField()),
                ('weight_end', models.IntegerField()),
            ],
        ),
    ]
