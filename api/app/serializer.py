from .models import Datamodel
from rest_framework import serializers


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datamodel
        fields = '__all__'