# Generated by Django 3.2.18 on 2023-09-06 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ammo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('compact', 'compact'), ('medium', 'medium'), ('long', 'long'), ('special', 'special'), ('shotgun', 'shotgun'), ('incendiary', 'incendiary'), ('poison', 'poison'), ('high velocity', 'high velocity'), ('spitzer', 'spitzer'), ('dumdum', 'badumdumsic'), ('FMJ', 'FMJ'), ('explosive', 'explosive'), ('flechette', 'flechette'), ('slug', 'slug'), ('dragonbreath', 'dragonbreath'), ('penny shot', 'penny shot'), ('starshell', 'starshell'), ('shredder', 'shredder'), ('poison bolt', 'poison bolt'), ('chaos bolt', 'chaos bolt'), ('choke bolt', 'choke bolt'), ('explosive bolt', 'explosive bolt'), ('shot bolt', 'shot bolt')], max_length=100, null=True)),
                ('price_ammo', models.IntegerField(blank=True, null=True)),
                ('damage', models.IntegerField(blank=True, null=True)),
                ('effectiverange', models.IntegerField(blank=True, null=True)),
                ('muzzle_velocity', models.IntegerField(blank=True, null=True)),
                ('verticalrecoil', models.IntegerField(blank=True, null=True)),
                ('capacity_magazine', models.IntegerField(blank=True, null=True)),
                ('capacity_spare', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cost', models.IntegerField(blank=True, null=True)),
                ('weapon_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.CharField(choices=[('compact', 'compact'), ('medium', 'medium'), ('long', 'long'), ('special', 'special'), ('shotgun', 'shotgun')], max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('rateoffire', models.IntegerField(blank=True, null=True)),
                ('cycletime', models.IntegerField(blank=True, null=True)),
                ('spread', models.IntegerField(blank=True, null=True)),
                ('sway', models.IntegerField(blank=True, null=True)),
                ('reloadspeed', models.IntegerField(blank=True, null=True)),
                ('meleedamage', models.IntegerField(blank=True, null=True)),
                ('heavymeleedamage', models.IntegerField(blank=True, null=True)),
                ('staminaconsumption', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Damagerange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dist_5', models.IntegerField()),
                ('dist_10', models.IntegerField()),
                ('dist_15', models.IntegerField()),
                ('dist_20', models.IntegerField()),
                ('dist_25', models.IntegerField()),
                ('dist_30', models.IntegerField()),
                ('dist_35', models.IntegerField()),
                ('dist_40', models.IntegerField()),
                ('dist_45', models.IntegerField()),
                ('dist_50', models.IntegerField()),
                ('dist_60', models.IntegerField()),
                ('dist_70', models.IntegerField()),
                ('dist_80', models.IntegerField()),
                ('dist_90', models.IntegerField()),
                ('dist_100', models.IntegerField()),
                ('dist_150', models.IntegerField()),
                ('dist_200', models.IntegerField()),
                ('dist_250', models.IntegerField()),
                ('ammo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='damage_range', to='api.ammo')),
            ],
        ),
        migrations.AddField(
            model_name='ammo',
            name='weapon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ammo', to='api.weapon'),
        ),
    ]