from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from ..serializers import NominationSerializer
from ..models import Nomination, Voting

class ApprovalView(APIView):
    permission_classes = [IsAdminUser]
    def get_nomination(self, id):
        try:
            return Nomination.objects.get(id=id)
        except Nomination.DoesNotExist:
            raise Http404
    
    def get(self, request, id):
        nomination = self.get_nomination(id)
        nomination.acceptance = True
        nomination.save()
        return Response(nomination, status=status.HTTP_200_OK)


class ContestantsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        nominations = Nomination.objects.filter(acceptance=True).all()
        serializer = NominationSerializer(nominations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# for these routes, any authenticated user can vote for his preferred candidate
class VotingView(APIView):
    permission_classes = [IsAuthenticated]
    def get_nominee(self, id):
        try:
            return Nomination.objects.get(id=id)
        except Voting.DoesNotExist:
            raise Http404
 
        
    
    def get(self, request, id):
        nominee = self.get_nominee(id)
        voting = Voting(
            contestant = nominee.nominee,
            voter = request.user
        )
        voting.save()
        return Response(voting, status=status.HTTP_400_BAD_REQUEST)
    

    
    