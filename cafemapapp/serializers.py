from rest_framework.serializers import ModelSerializer
from .models import Hashtags

class TestDataSerializer(ModelSerializer):
   class Meta:
       model = Hashtags
       fields = '__all__'