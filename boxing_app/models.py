from pyexpat import model
from django.db import models

# Create your models here.
# class Trenerlar(models.Model):
#     fio = models.CharField(max_length=200)

class Viloyatlar(models.Model):
    viloyat_nomi_uz = models.CharField(max_length=200)
    viloyat_nomi_ru = models.CharField(max_length=200)
    viloyat_nomi_en = models.CharField(max_length=200)

    def __str__(self):
        return self.viloyat_nomi_uz

class All_types_of_chempion(models.Model):
    type_uz = models.CharField(max_length=200, default='')
    type_ru = models.CharField(max_length=200, default='')
    type_en = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.type_uz


class Boxer(models.Model):
    fio = models.CharField(max_length=200)
    nomeri = models.CharField(max_length=200)
    turar_joyi = models.CharField(max_length=200)
    umumiy_janglari_soni = models.CharField(max_length=200, default='')
    yutganlari = models.CharField(max_length=200, default='')
    yutqazganlari = models.CharField(max_length=200, default='')
    nokaut = models.CharField(max_length=200, default='')
    taqdim_etish_orqali = models.CharField(max_length=200, default='')
    qaror = models.CharField(max_length=200, default='')
    viloyat = models.ForeignKey(Viloyatlar, on_delete=models.CASCADE)
    unvoni = models.ForeignKey(All_types_of_chempion, null=True, blank=True, on_delete=models.CASCADE)
    trener_1 = models.CharField(max_length=200, default='None')
    trener_2 = models.CharField(max_length=200, default='None')
    trener_3 = models.CharField(max_length=200, default='None')
    trener_4 = models.CharField(max_length=200, default='None')
    trener_5 = models.CharField(max_length=200, default='None')
    boxer_rasmi = models.ImageField(upload_to="uploads/boxers/", height_field=None, width_field=None, max_length=100)
    passport_pdf = models.FileField(upload_to ="uploads/passport/")


    def __str__(self):
        return self.fio



