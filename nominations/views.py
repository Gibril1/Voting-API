from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import NominationSerializer
from .models import Nomination
from portfolios.models import Portfolio
from elections.models import Election
from project.permissions import UserEditDeletePermission

# Create your views here.
class NominationView(APIView):
    permission_classes = [IsAuthenticated]

    def get_portfolio(self, id):
        try:
            return Portfolio.objects.get(id=id)
        except Portfolio.DoesNotExist:
            raise Http404    
    def get_election(self, id):
        try:
            return Election.objects.get(id=id)
        except Election.DoesNotExist:
            raise Http404   

    def check_if_nominated_already(self,user, election):
        return Nomination.objects.filter(nominee=user).filter(election = election ).first()
        

    # for filing nomnation forms
    def get(self, request, id):
        portfolio = self.get_portfolio(id)
        election =  self.get_election(portfolio.election.id)
        already_picked_nomination = self.check_if_nominated_already(request.user, election)

        if already_picked_nomination:
            message = 'You cannot pick two nominations'
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        try:
            nomination = Nomination.objects.create(
                portfolio = portfolio,
                nominee = request.user,
                acceptance = False,
                election = election
            )
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        serializer = NominationSerializer(nomination)  
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class NominationDetailView(RetrieveUpdateDestroyAPIView, UserEditDeletePermission):
    permission_classes = [UserEditDeletePermission]
    queryset = Nomination.objects.all()
    serializer_class = NominationSerializer
