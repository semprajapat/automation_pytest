from django.shortcuts import render
from .models import Datamodel
from .serializer import DataSerializer
from rest_framework import viewsets
# Create your views here.


class DataView(viewsets.ModelViewSet):
    serializer_class = DataSerializer
    queryset = Datamodel.objects.all()