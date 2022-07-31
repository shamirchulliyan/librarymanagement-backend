from lib2to3.pgen2.pgen import DFAState
from django.core.management.base import BaseCommand
import pandas as pd
from LIB.models import *

class Command(BaseCommand):
    help = 'import booms'
    
    def add_arguments(self, parser):
        pass
    
    def handle(self, *args, **options):
        df = pd.read_csv('LibDB.csv')
        for BOOKNUMBER,BOOKNAME,NAMEOFAUTHOR,NAMEOFPUBLISHER,COSTOFBOOK,DATEOFENTRY,STATUSOFBOOK,SOURCEOFBOOK,RACKNUMBER,CATEGORY in zip(df.BOOKNUMBER,df.BOOKNAME,df.NAMEOFAUTHOR,df.NAMEOFPUBLISHER,df.COSTOFBOOK,df.DATEOFENTRY,df.STATUSOFBOOK,df.SOURCEOFBOOK,df.RACKNUMBER,df.CATEGORY):
            models = Book(BookNo = BOOKNUMBER, BookName = BOOKNAME, AuthorName = NAMEOFAUTHOR, PublisherName = NAMEOFPUBLISHER, CostofBook = COSTOFBOOK, DateofEntry = DATEOFENTRY, StatusofBook = STATUSOFBOOK, SourceofBook = SOURCEOFBOOK, RackNo = RACKNUMBER, Category = CATEGORY)
            models.save()