# Generated by Django 4.1.1 on 2022-09-15 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boxing_app', '0005_remove_viloyatlar_viloyat_nomi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viloyatlar',
            name='viloyat_nomi_en',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='viloyatlar',
            name='viloyat_nomi_ru',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='viloyatlar',
            name='viloyat_nomi_uz',
            field=models.CharField(max_length=200),
        ),
    ]