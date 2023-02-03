from rest_framework import serializers
from .models import (
   
    Voting, 
    Portfolio,  
    Election
)



class VotingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voting
        fields = '__all__'
        read_only_fields = ['contestant', 'voter']

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'



