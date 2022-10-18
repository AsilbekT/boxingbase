from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = 'Boxing Federation'
admin.site.register(Boxer)
admin.site.register(Viloyatlar)
admin.site.register(All_types_of_chempion)