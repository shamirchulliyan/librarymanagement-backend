from dataclasses import fields
from rest_framework import serializers
from .models import *

class CountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Count
        fields = ('id', 'Book_Name', 'count')
        