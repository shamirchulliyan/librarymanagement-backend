from django.contrib import admin
from .models import *

# Register your models here.
class BooksAdminModel(admin.ModelAdmin):
    search_fields=('BookNo', 'BookName', 'AuthorName',)

admin.site.register(Book,BooksAdminModel)