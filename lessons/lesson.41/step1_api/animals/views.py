from rest_framework.viewsets import ModelViewSet
from .models import Animal
from .serializers import AnimalSerializer

# Create your views here.
class AnimalViewSet(ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer