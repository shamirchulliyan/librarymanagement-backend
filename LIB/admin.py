from django.contrib import admin
from .models import *

# Register your models here.
class BooksAdminModel(admin.ModelAdmin):
    search_fields=('BookNo', 'BookName', 'AuthorName',)

class CountAdminModel(admin.ModelAdmin):
    search_fields = ('Book_Name',)

admin.site.register(Book,BooksAdminModel)
admin.site.register(Count,CountAdminModel)