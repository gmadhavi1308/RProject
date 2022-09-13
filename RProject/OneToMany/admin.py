from django.contrib import admin
from OneToMany.models import *
class SongAdmin(admin.ModelAdmin):
    list_display = ['title','album']
admin.site.register(Album)
admin.site.register(Song,SongAdmin)
# Register your models here.
