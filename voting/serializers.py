from rest_framework import serializers
from .models import Nomination, Voting, Portfolio

class NominationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nomination
        fields = '__all__'
        read_only_fields = ['nominee']

class VotingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voting
        fields = '__all__'
        read_only_fields = ['contestant', 'voter']

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'