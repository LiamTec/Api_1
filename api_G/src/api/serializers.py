from rest_framework import serializers
from .models import Supervivientes, Zombies, Gun

class SupervivientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervivientes
        fields = '__all__'

class ZombiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zombies
        fields = '__all__'

class GunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gun
        fields = '__all__'
