from django.urls import path, include
from rest_framework import routers
from .views import SupervivientesViewSet, ZombiesViewSet, GunViewSet

router = routers.DefaultRouter()
router.register(r'supervivientes', SupervivientesViewSet)
router.register(r'zombies', ZombiesViewSet)
router.register(r'guns', GunViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
