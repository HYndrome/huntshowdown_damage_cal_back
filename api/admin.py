from django.contrib import admin
from .models import Weapon, Ammo, Damagerange
# Register your models here.

admin.site.register(Weapon)
admin.site.register(Ammo)
admin.site.register(Damagerange)
