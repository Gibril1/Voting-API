from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..serializers import VotingSerializer
from ..models import Nomination, Voting, Candidate

class ApprovalView(APIView):
    def get_nomination(self, id):
        try:
            return Nomination.objects.get(id=id)
        except Nomination.DoesNotExist:
            raise Http404
    
    def get(self, request, id):
        nomination = self.get_nomination(id)
        nomination.acceptance = True
        nomination.save()

        candidate = Candidate(
            nomination = nomination
        )

        candidate.save()
        return Response(candidate, status=status.HTTP_200_OK)

# for these routes, any authenticated user can vote for his preferred candidate
class VotingView(APIView):
    permission_classes = [IsAuthenticated]
    def get_nominee(self, id):
        try:
            return Voting.objects.get(id=id)
        except Voting.DoesNotExist:
            raise Http404
 
        
    
    def get(self, request, id):
        nominee = self.get_nominee(id)
        nominee.votes+=1
        serializer = VotingSerializer(nominee, data=request.data)
        if serializer.is_valid():
            serializer.save(voter=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
    