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
from project.permissions import UserEditDeletePermission

# Create your views here.
class NominationView(APIView):
    permission_classes = [IsAuthenticated]

    def get_portfolio(self, id):
        try:
            return Portfolio.objects.get(id=id)
        except Portfolio.DoesNotExist:
            raise Http404    

    # for filing nomnation forms
    def get(self, request, id):
        portfolio = self.get_portfolio(id)
        nomination = Nomination.objects.create(
            portfolio = portfolio,
            nominee = request.user,
            acceptance = False
        )
        serializer = NominationSerializer(nomination)
        if nomination:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NominationDetailView(RetrieveUpdateDestroyAPIView, UserEditDeletePermission):
    permission_classes = [UserEditDeletePermission]
    queryset = Nomination.objects.all()
    serializer_class = NominationSerializer
