from rest_framework import serializers
from .models import Weapon, Ammo, Damagerange

class DamagerangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Damagerange
        fields = ['dist_5','dist_10','dist_15','dist_20','dist_25','dist_30','dist_35','dist_40','dist_45','dist_50','dist_60','dist_70','dist_80','dist_90','dist_100','dist_150','dist_200','dist_250',]

class AmmoSerializer(serializers.ModelSerializer):
    damage_range = DamagerangeSerializer(many=True, read_only=True)
    class Meta:
        model = Ammo
        fields = '__all__'


class WeaponSerializer(serializers.ModelSerializer):
    weapon_image = serializers.ImageField(use_url=True)
    ammo = AmmoSerializer(many=True, read_only=True)
    class Meta:
        model = Weapon
        fields = '__all__'