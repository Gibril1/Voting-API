from rest_framework.serializers import ModelSerializer
from .models import Nomination

class NominationSerializer(ModelSerializer):
    class Meta:
        model = Nomination
        fields = '__all__'
        read_only_fields = ['nominee']