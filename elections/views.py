from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Election
from .serializers import ElectionSerializer
from project.permissions import UserEditDeletePermission


class CreateElectionView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ElectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(createdBy=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListElectionsView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset =  Election.objects.all()
    serializer_class = ElectionSerializer


class ElectionDetailView(RetrieveUpdateDestroyAPIView, UserEditDeletePermission):
    permission_classes = [UserEditDeletePermission]
    queryset =  Election.objects.all()
    serializer_class = ElectionSerializer