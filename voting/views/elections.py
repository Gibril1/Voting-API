from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, BasePermission, SAFE_METHODS
from rest_framework.response import Response
from ..serializers import ElectionSerializer
from ..models import Election


class UserEditDeletePermission(BasePermission):
    message = 'Editing nominations is just for the user who created it'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        return obj.nominee == request.user
        
class ElectionView(APIView):
    permission_classes=[IsAdminUser]

    def get(self, request):
        elections = Election.objects.all()
        serializer = ElectionSerializer(elections, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ElectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(createdBy = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ElectionDetailView(APIView):
    permission_classes = [IsAdminUser]
    def get_election(self, id):
        try: 
            return Election.objects.get(id=id)
        except Election.DoesNotExist:
            raise Http404

    
    def get(self, request, id):
        election = self.get_election(id)
        serializer = ElectionSerializer(election)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        election = self.get_election(id)
        serializer = ElectionSerializer(election, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, id):
        election = self.get_election(id)
        election.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




