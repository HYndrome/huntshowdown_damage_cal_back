from django.db import models

# Create your models here.
WEAPON_CHOICES = (
    ("compact", "compact"),
    ("medium", "medium"),
    ("long", "long"),
    ("special", "special"),
    ("shotgun", "shotgun"),
)

class Weapon(models.Model):
    name = models.CharField(max_length = 100)
    cost = models.IntegerField(blank=True, null=True)
    weapon_image = models.ImageField(blank=True, null=True)
    category = models.CharField(
        max_length = 100,
        choices=WEAPON_CHOICES
    )
    description = models.TextField(blank=True, null=True)
    rateoffire = models.FloatField(blank=True, null=True)
    cycletime = models.FloatField(blank=True, null=True)
    spread = models.FloatField(blank=True, null=True)
    sway = models.FloatField(blank=True, null=True)

    reloadspeed = models.FloatField(blank=True, null=True)
    meleedamage = models.IntegerField(blank=True, null=True)
    heavymeleedamage = models.IntegerField(blank=True, null=True)
    staminaconsumption = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

AMMO_CHOICES = (
    ("compact", "compact"),
    ("medium", "medium"),
    ("long", "long"),
    ("special", "special"),
    ("shotgun", "shotgun"),
    ("incendiary", "incendiary"),
    ("poison", "poison"),
    ("high velocity", "high velocity"),
    ("spitzer", "spitzer"),
    ("dumdum", "dumdum"),
    ("FMJ", "FMJ"),
    ("explosive", "explosive"),
    ("flechette", "flechette"),
    ("slug", "slug"),
    ("dragonbreath", "dragonbreath"),
    ("penny shot", "penny shot"),
    ("starshell", "starshell"),
    ("shredder", "shredder"),
    ("poison bolt", "poison bolt"),
    ("chaos bolt", "chaos bolt"),
    ("choke bolt", "choke bolt"),
    ("explosive bolt", "explosive bolt"),
    ("shot bolt", "shot bolt"),
)

class Ammo(models.Model):
    weapon = models.ManyToManyField(Weapon, related_name="ammo")
    type = models.CharField(
        max_length = 100,
        choices=AMMO_CHOICES,
        blank=True,
        null=True,
    )
    price_ammo = models.IntegerField(blank=True, null=True)
    damage = models.IntegerField(blank=True, null=True)
    effectiverange = models.IntegerField(blank=True, null=True)
    muzzle_velocity = models.IntegerField(blank=True, null=True)
    verticalrecoil = models.FloatField(blank=True, null=True)
    capacity_magazine = models.IntegerField(blank=True, null=True)
    capacity_spare = models.IntegerField(blank=True, null=True)

class Damagerange(models.Model):
    ammo = models.ManyToManyField(Ammo, related_name="damage_range")
    dist_5 = models.IntegerField()
    dist_10 = models.IntegerField()
    dist_15 = models.IntegerField()
    dist_20 = models.IntegerField()
    dist_25 = models.IntegerField()
    dist_30 = models.IntegerField()
    dist_35 = models.IntegerField()
    dist_40 = models.IntegerField()
    dist_45 = models.IntegerField()
    dist_50 = models.IntegerField()
    dist_60 = models.IntegerField()
    dist_70 = models.IntegerField()
    dist_80 = models.IntegerField()
    dist_90 = models.IntegerField()
    dist_100 = models.IntegerField()
    dist_150 = models.IntegerField()
    dist_200 = models.IntegerField()
    dist_250 = models.IntegerField()