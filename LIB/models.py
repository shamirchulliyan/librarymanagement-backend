from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Book(models.Model):
    BookNo = models.IntegerField(_("BOOK NUMBER"),primary_key = True)
    BookName = models.CharField(_('BOOK NAME'),max_length=200)
    AuthorName = models.CharField(_('NAME OF AUTHOR'),max_length=200)
    PublisherName = models.CharField(_('NAME OF PUBLISHER'),max_length=200, null = True, blank = True)
    CostofBook = models.IntegerField(_('COST OF BOOK'),null = True, blank = True)
    DateofEntry = models.DateField(_('DATE OF ENTRY'), null = True, blank = True)
    StatusofBook = models.CharField(_('STATUS OF BOOK'),max_length=50)
    SourceofBook = models.CharField(_('SOURCE OF BOOK'),max_length=200, null = True, blank = True)
    RackNo = models.IntegerField(_('RACK NUMBER'),null = True, blank = True)
    Category = models.CharField(_('CATEGORY'),max_length = 200, null = True, blank = True)
    
    def __str__(self):
        return self.BookName

class Count(models.Model):
    Book_Name = models.CharField(_('Book Name'),max_length=200)
    Count = models.IntegerField(_('Count'))
    