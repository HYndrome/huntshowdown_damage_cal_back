from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('weapon', views.WeaponViewSet)

urlpatterns = [
    path('', include(router.urls))
]
