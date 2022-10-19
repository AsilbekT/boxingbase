from django.shortcuts import redirect, render

from boxing_app.forms import BoxerForm
from .models import *
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
from django.utils import translation
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    return render(request, "admin_lte/index.html")


def main_page(request):
    regions = Viloyatlar.objects.all()
    boxers = Boxer.objects.all()
    weights = Different_weight.objects.all()
    all_types_of_chempion = All_types_of_chempion.objects.all()
    if request.method == "POST":
        regions_list = request.POST.getlist('regions')
        chempion_type = request.POST.getlist('chempion_type')
        chempion_weight = request.POST.getlist('weight')
        chempion_fio = request.POST.getlist('fio')

        if request.LANGUAGE_CODE == "uz":
            regions_list_obj = Viloyatlar.objects.filter(viloyat_nomi_uz__in=regions_list)
        elif request.LANGUAGE_CODE == "ru":
            regions_list_obj = Viloyatlar.objects.filter(viloyat_nomi_ru__in=regions_list)
        else:
            regions_list_obj = Viloyatlar.objects.filter(viloyat_nomi_en__in=regions_list)
        
        regions_list_obj_ids = [x.id for x in regions_list_obj]
        
        first = len(regions_list) > 0
        second = len(chempion_type) > 0
        third = len(chempion_weight) > 0
        fourth = len(chempion_fio[0]) > 0

        if first == True and second == False and third == False and fourth == False:
            boxers = Boxer.objects.filter(viloyat__in=regions_list_obj_ids)

            
        elif first == True and second == True and third == False and fourth == False:
            if request.LANGUAGE_CODE == "uz":
                chempion_people = All_types_of_chempion.objects.get(type_uz=chempion_type[0])
                boxers = chempion_people.boxer_set.filter(viloyat__in=regions_list_obj_ids)
            elif request.LANGUAGE_CODE == "ru":
                chempion_people = All_types_of_chempion.objects.get(type_ru=chempion_type[0])
                boxers = chempion_people.boxer_set.filter(viloyat__in=regions_list_obj_ids)
            else:
                chempion_people = All_types_of_chempion.objects.get(type_en=chempion_type[0])
                boxers = chempion_people.boxer_set.filter(viloyat__in=regions_list_obj_ids)
  
        elif first == True and second == False and third == True and fourth == False:
            chempion_weight = chempion_weight[0].split("-")
            weight_range_1 = int(chempion_weight[0])
            weight_range_2 = int(chempion_weight[1])
            
            if request.LANGUAGE_CODE == "uz":
                boxers = Boxer.objects.filter(viloyat__in=regions_list_obj_ids, vazni__range=[weight_range_1, weight_range_2])
            elif request.LANGUAGE_CODE == "ru":
                boxers = Boxer.objects.filter(viloyat__in=regions_list_obj_ids, vazni__range=[weight_range_1, weight_range_2])
            else:
                boxers = Boxer.objects.filter(viloyat__in=regions_list_obj_ids, vazni__range=[weight_range_1, weight_range_2])
        
        elif first == True and second == True and third == True:
            chempion_weight = chempion_weight[0].split("-")
            weight_range_1 = int(chempion_weight[0])
            weight_range_2 = int(chempion_weight[1])

            if request.LANGUAGE_CODE == "uz":
                chempion_people = All_types_of_chempion.objects.get(type_uz=chempion_type[0])
                boxers = chempion_people.boxer_set.filter(viloyat__in=regions_list_obj_ids, vazni__range=[weight_range_1, weight_range_2], )
            elif request.LANGUAGE_CODE == "ru":
                chempion_people = All_types_of_chempion.objects.get(type_ru=chempion_type[0])
                boxers = chempion_people.boxer_set.filter(viloyat__in=regions_list_obj_ids, vazni__range=[weight_range_1, weight_range_2])
            else:
                chempion_people = All_types_of_chempion.objects.get(type_en=chempion_type[0])
                boxers = chempion_people.boxer_set.filter(viloyat__in=regions_list_obj_ids, vazni__range=[weight_range_1, weight_range_2])
        
        elif  first == False and second == True and third == False and fourth == False:
            chempion_people = All_types_of_chempion.objects.get(type_uz=chempion_type[0])
            boxers = chempion_people.boxer_set.all()

        elif first == False and second == True and third == True and fourth == False:
            chempion_weight = chempion_weight[0].split("-")
            weight_range_1 = int(chempion_weight[0])
            weight_range_2 = int(chempion_weight[1])

            if request.LANGUAGE_CODE == "uz":
                chempion_people = All_types_of_chempion.objects.get(type_uz=chempion_type[0])
                boxers = chempion_people.boxer_set.filter(vazni__range=[weight_range_1, weight_range_2])
            elif request.LANGUAGE_CODE == "ru":
                chempion_people = All_types_of_chempion.objects.get(type_ru=chempion_type[0])
                boxers = chempion_people.boxer_set.filter(vazni__range=[weight_range_1, weight_range_2])
            else:
                chempion_people = All_types_of_chempion.objects.get(type_en=chempion_type[0])
                boxers = chempion_people.boxer_set.filter(vazni__range=[weight_range_1, weight_range_2])
            
        elif first == False and second == False and third == True and fourth == False:
            chempion_weight = chempion_weight[0].split("-")
            weight_range_1 = int(chempion_weight[0])
            weight_range_2 = int(chempion_weight[1])
            boxers = Boxer.objects.filter(vazni__range=[weight_range_1, weight_range_2])

        elif first == False and second == False and third == False and fourth == True:
            boxers = Boxer.objects.filter(fio__contains=chempion_fio[0])




    context = {"boxers": boxers, "regions": regions, 'chempion_type': all_types_of_chempion, "weights": weights}
    return render(request, "admin_lte/data.html", context)


def boxers_details(request, id):
    boxer = Boxer.objects.get(id=id)


    context = {"boxer": boxer}
    return render(request, "details/index.html", context)


def edit_boxer(request, id):
    boxer = Boxer.objects.get(id=id)

    context = {"boxer": boxer}
    return render(request, "details/form_edit.html", context)


def add_boxer(request):
    
    if request.method == "POST":
        form = BoxerForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            form.save()
    form = BoxerForm()

    context = {"form": form}
    return render(request, "details/form.html", context)


def login_page(request):
    context = {}
    return render(request, "admin_lte/login.html", context)




def change_lang(request):
    LANGUAGE_SESSION_KEY = '_language'
    if request.method == "POST":
        sent_url = request.POST['next']
        old_lang = request.LANGUAGE_CODE
        changed_lang = request.POST['language']
        translation.activate(changed_lang)
        request.session[LANGUAGE_SESSION_KEY] = changed_lang
        # # I use HTTP_REFERER to direct them back to previous path 
        if "en" in sent_url:
            if changed_lang != 'uz':
                new_url = sent_url.replace('en', changed_lang)
                return HttpResponseRedirect(new_url)
            elif changed_lang == 'uz':
                new_url1 = sent_url.replace('en', '')
                new_url = new_url1[1:]
                return HttpResponseRedirect(new_url)
        elif "ru" in sent_url:
            if changed_lang != 'uz':
                new_url = sent_url.replace('ru', changed_lang)
                return HttpResponseRedirect(new_url)
            elif changed_lang == 'uz':
                new_url1 = sent_url.replace('ru', '')
                new_url = new_url1[1:]
                return HttpResponseRedirect(new_url)
        elif old_lang == "uz" and changed_lang != 'uz':
            new_url = f"/{changed_lang}" + sent_url

            return HttpResponseRedirect(new_url)
        
        return HttpResponseRedirect(sent_url)
