from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Portfolio
from elections.models import Election
from .serializers import PortfolioSerializer
from project.permissions import UserEditDeletePermission

# Create your views here.
class CreatePortfolioView(APIView):
    def get_election(self, id):
        try:
            return Election.objects.get(id=id)
        except Election.DoesNotExist:
            raise Http404

    def post(self, request, id):
        election = self.get_election(id)
        data = request.data
        if election.createdBy != request.user:
            message = 'You cannot create portfolios for this election'
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        portfolio_name_exists = Portfolio.objects.filter(portfolio=data['portfolio']).filter(election=election).first()

        if portfolio_name_exists:
            message = f"Portfolio  with portfolio name {data['portfolio']} already exists"
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        portfolio = Portfolio.objects.create(
            election = election,
            description = data['description'],
            category = data['category'],
            portfolio = data['portfolio'],
            createdBy = request.user
        )
        serializer = PortfolioSerializer(portfolio)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class ListPortfoliosView(ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class =  PortfolioSerializer


class PortfolioDetailsView(RetrieveUpdateDestroyAPIView, UserEditDeletePermission):
    permission_classes = [UserEditDeletePermission]
    queryset = Portfolio.objects.all()
    serializer_class =  PortfolioSerializer

