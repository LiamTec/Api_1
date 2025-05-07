from rest_framework import viewsets
from .models import Supervivientes, Zombies, Gun
from .serializers import SupervivientesSerializer, ZombiesSerializer, GunSerializer

class SupervivientesViewSet(viewsets.ModelViewSet):
    queryset = Supervivientes.objects.all()
    serializer_class = SupervivientesSerializer

class ZombiesViewSet(viewsets.ModelViewSet):
    queryset = Zombies.objects.all()
    serializer_class = ZombiesSerializer

class GunViewSet(viewsets.ModelViewSet):
    queryset = Gun.objects.all()
    serializer_class = GunSerializer
