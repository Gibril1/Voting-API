from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from voting.serializers import NominationSerializer, PortfolioSerializer
from voting.models import Nomination, Portfolio


class PortfolioView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = PortfolioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        portfolios = Portfolio.objects.all()
        serializer = PortfolioSerializer(portfolios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PortfolioDetailsView(APIView):
    def get_portfolio(self, id):
        try:
            return Nomination.objects.get(id=id)
        except Nomination.DoesNotExist:
            raise Http404

    def get(self, request, id):
        portfolio = self.get_portfolio(id)
        serializer = NominationSerializer(portfolio)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        portfolio = self.get_portfolio(id)

        serializer = PortfolioSerializer(portfolio, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        portfolio = self.get_portfolio(id)
        portfolio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

