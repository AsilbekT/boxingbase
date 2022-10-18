# Generated by Django 4.1.1 on 2022-09-12 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boxer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=200)),
                ('nomeri', models.CharField(max_length=200)),
                ('turar_joyi', models.CharField(max_length=200)),
                ('viloyat', models.CharField(max_length=200)),
                ('boxer_rasmi', models.ImageField(upload_to='uploads/boxers/')),
                ('passport_pdf', models.FileField(upload_to='uploads/passport/')),
            ],
        ),
    ]
