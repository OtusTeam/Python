from rest_framework.serializers import ModelSerializer
from .models import Animal


class AnimalSerializer(ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'
