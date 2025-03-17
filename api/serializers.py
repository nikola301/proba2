from rest_framework import serializers
from .models import Helikopteri

class HelikopteriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Helikopteri
        fields = '__all__'  # Includes all fields
