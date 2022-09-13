from django.contrib import admin
from OneToOne.models import *

class PersonAdmin(admin.ModelAdmin):
    list_display = ['name','contact']
admin.site.register(Idproof)
admin.site.register(Person,PersonAdmin)
# Register your models here.
