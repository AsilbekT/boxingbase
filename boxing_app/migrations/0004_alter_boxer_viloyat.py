# Generated by Django 4.1.1 on 2022-09-15 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boxing_app', '0003_viloyatlar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boxer',
            name='viloyat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boxing_app.viloyatlar'),
        ),
    ]