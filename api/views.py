from django.shortcuts import render
from rest_framework import viewsets
from .serializers import WeaponSerializer
from .models import Weapon

# Create your views here.
class WeaponViewSet(viewsets.ModelViewSet):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer