from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import NominationSerializer
from .models import Nomination

# Create your views here.
class NominationView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        nominees = Nomination.objects.all()
        serializer = NominationSerializer(nominees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = NominationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(nominee=request.user)
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NominationDetailView(APIView):
    permission_classes = [IsAuthenticated]
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


