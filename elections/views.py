from django.http import Http404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Election
from .serializers import ElectionSerializer

class ElectionView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset =  Election.objects.all()
    serializer_class = ElectionSerializer


class ElectionDetailView(RetrieveUpdateDestroyAPIView):
    queryset =  Election.objects.all()
    serializer_class = ElectionSerializer