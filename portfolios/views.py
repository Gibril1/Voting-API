from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Portfolio
from .serializers import PortfolioSerializer
from project.permissions import UserEditDeletePermission

# Create your views here.
class PortfolioView(ListCreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class =  PortfolioSerializer


class PortfolioDetailsView(RetrieveUpdateDestroyAPIView, UserEditDeletePermission):
    permission_classes = [UserEditDeletePermission]
    queryset = Portfolio.objects.all()
    serializer_class =  PortfolioSerializer

