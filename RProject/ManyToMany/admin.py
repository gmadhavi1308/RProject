from django.contrib import admin
from ManyToMany.models import *
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title','id']
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
# Register your models here.
