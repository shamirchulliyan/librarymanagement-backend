from django.db import models
from django.utils.translation import gettext as _
from sre_constants import CATEGORY
from unicodedata import category

# Create your models here.

class Book(models.Model):
    BookNo = models.IntegerField(_("BOOK NUMBER"),primary_key = True)
    BookName = models.CharField(_('BOOK NAME'),max_length=200)
    AuthorName = models.CharField(_('NAME OF AUTHOR'),max_length=200, null = True)
    PublisherName = models.CharField(_('NAME OF PUBLISHER'),max_length=200, null = True, blank=True)
    CostofBook = models.IntegerField(_('COST OF BOOK'),null = True, blank=True)
    DateofEntry = models.DateField(_('DATE OF ENTRY'),auto_now= True, null = True, blank=True)
    StatusofBook = models.CharField(_('STATUS OF BOOK'),max_length=50, null = True, blank=True)
    SourceofBook = models.CharField(_('SOURCE OF BOOK'),max_length=200, null = True, blank=True)
    RackNo = models.IntegerField(_('RACK NUMBER'),null = True, blank=True)
    Category = models.CharField(_('CATEGORY'),max_length = 200, null = True, blank=True)
    
    def __str__(self):
        return self.BookName

class Count(models.Model):
    Book_Name = Book.objects.all().values_list('BookName').distinct()
    count = Book.objects.all().values_list('BookName').distinct().count()

class Issue(models.Model):
    CATEGORY = (
        ('YES', 'YES'),
        ('NO', 'NO'),
    )
    BookNo = models.IntegerField(_('Book Number'))
    BookName = models.CharField(_('Book Name'), max_length=200)
    AuthorName = models.CharField(_("Author Name"), max_length=200)
    RegId = models.CharField(_("Register Id"), max_length=50)
    IssuedDate = models.DateField(_("Issued Date"), auto_now=False, auto_now_add=True)
    IsReturned = models.CharField(_("IS RETURNED"), max_length=50, choices = CATEGORY)
    
    def __str__(self):
        return self.BookName