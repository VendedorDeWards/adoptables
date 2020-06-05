from rest_framework.generics import ListAPIView, RetrieveAPIView

from catalog.models import Pet
from .serializers import PetSerializer

class PetListView(ListAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class PetDetailView(ListAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer