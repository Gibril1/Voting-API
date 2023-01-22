from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework.response import Response
from ..serializers import NominationSerializer
from ..models import Nomination, Portfolio

class UserEditDeletePermission(BasePermission):
    message = 'Editing nominations is just for the user who created it'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        return obj.nominee == request.user

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
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        




# these routes are for the user to edit the details of his/her nomination
class NominationDetailView(APIView, UserEditDeletePermission):
    permission_classes = [UserEditDeletePermission]
    def get_nomination(self, id):
        try:
            return Nomination.objects.get(id=id)
        except Nomination.DoesNotExist:
            raise Http404

    def get(self, request, id):
        nomination = self.get_nomination(id)
        serializer = NominationSerializer(nomination)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        nomination = self.get_nomination(id)
        serializer = NominationSerializer(nomination, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        nomination = self.get_nomination(id)
        nomination.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    

    
        