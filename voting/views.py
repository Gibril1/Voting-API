from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.serializers import UserSerializer
from nominations.models import Nomination
from .serializers import VotingSerializer
from elections.models import Election
from .models import  Voting

class ApprovalView(APIView):
    def get_nomination(self, id):
        try:
            return Nomination.objects.get(id=id)
        except Nomination.DoesNotExist:
            raise Http404

    def get_election(self, id):
        try:
            return Election.objects.get(id=id)
        except Election.DoesNotExist:
            raise Http404
    
    def head(self, request, id):
        nomination = self.get_nomination(id)
        election = self.get_election(nomination.election.id)
        if election.createdBy != request.user:
            message = 'You are not authorized'
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        nomination.acceptance = True
        nomination.save()
        return Response(status=status.HTTP_200_OK)


class ContestantsView(APIView):
    # permission_classes = [IsAuthenticated]

    def get_election(self, id):
        try:
            return Election.objects.get(id=id)
        except Election.DoesNotExist:
            raise Http404

    def get(self, request, id):
        election = self.get_election(id)
        nominations = Nomination.objects.filter(acceptance=True).filter(election=election).all()
        users = User.objects.filter(id__in=[nomination.nominee.id for nomination in nominations]).all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class VotingView(APIView):
    permission_classes = [IsAuthenticated]
    def get_nominee(self, id):
        try:
            return Nomination.objects.get(id=id)
        except Voting.DoesNotExist:
            raise Http404
    
    def get_election(self, id):
        try:
            return Election.objects.get(id=id)
        except Election.DoesNotExist:
            raise Http404
 
        
    
    def get(self, request, id):
        nominee = self.get_nominee(id)
        election = self.get_election(nominee.election.id)
        if nominee.acceptance == False:
            message = 'This nominee is not qualified'
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        voting = Voting(
            contestant = nominee.nominee,
            voter = request.user,
            election =  election
        )
        voting.save()
        serializer = VotingSerializer(voting)
        if voting:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
    