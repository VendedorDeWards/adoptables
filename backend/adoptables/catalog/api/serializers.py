from rest_framework import serializers
from catalog.models import Pet


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Pet