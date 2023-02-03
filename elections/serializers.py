from rest_framework.serializers import ModelSerializer
from .models import Election

class ElectionSerializer(ModelSerializer):
    class Meta:
        model = Election
        fields = '__all__'