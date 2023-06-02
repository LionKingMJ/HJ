from rest_framework import serializers
from .models import *

class LionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Lion
    fields = '__all__'