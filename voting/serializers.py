from rest_framework import serializers
from .models import (
   
    Voting, 
    
)



class VotingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voting
        fields = '__all__'
        read_only_fields = ['contestant', 'voter']




