from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from .models import *

# Create your views here.


class CountView(viewsets.ModelViewSet):
    serializer_class = CountSerializer
    queryset = Count.objects.all()
    
