from rest_framework.serializers import ModelSerializer
from .models import Studycafes

class TestDataSerializer(ModelSerializer):
    class Meta:
        model = Studycafes
        fields = '__all__'