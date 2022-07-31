from django.contrib import admin
from .models import *

# Register your models here.
class BooksAdminModel(admin.ModelAdmin):
    search_fields=('BookNo', 'BookName', 'AuthorName',)

class IssueAdminModel(admin.ModelAdmin):
    search_fields = ('BookNo', 'BookName', 'RegId')


admin.site.register(Book,BooksAdminModel)
admin.site.register(Issue, IssueAdminModel)