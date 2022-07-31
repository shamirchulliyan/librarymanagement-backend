from django.shortcuts import render
from .serializers import CountSerializer
from rest_framework import viewsets
from .models import Count

# Create your views here.

class CountView(viewsets.ModelViewSet):
    serializer_class = CountSerializer
    queryset = Count.objects.all()