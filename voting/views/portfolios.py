from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, BasePermission, SAFE_METHODS
from rest_framework.response import Response
from voting.serializers import  PortfolioSerializer
from voting.models import  Portfolio, Election

class UserEditDeletePermission(BasePermission):
    message = 'Editing portfolio is just for the user who created it'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        return obj.nominee == request.user


class PortfolioView(APIView):
    permission_classes = [IsAdminUser]

    def get_election(self, id):
        try:
            return Election.objects.get(id=id)
        except Election.DoesNotExist:
            raise Http404

    # creates a portfolio for a particular election
    def post(self, request, id):
        
        # check if election exists and gets the request data
        election = self.get_election(id)
        data = request.data

        # checks to see if the name for that portfolio already exists in the election
        portfolioExists = Portfolio.objects.filter(portfolio=data['portfolio']).filter(election = election).first()

        if portfolioExists:
            message = f"Portfolio with name { data['portfolio'] } already exists"
            return Response(message, status=status.HTTP_404_NOT_FOUND)

        # create the portfolio
        portfolio = Portfolio.objects.create(
            portfolio = data['portfolio'],
            description = data['description'],
            category = data['category'],
            election = election
        )
        serializer = PortfolioSerializer(portfolio)
        if portfolio:     
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        election = self.get_election(id)
        portfolios = Portfolio.objects.filter(election=election).all()
        serializer = PortfolioSerializer(portfolios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PortfolioDetailsView(APIView, UserEditDeletePermission):
    permission_classes = [UserEditDeletePermission]
    def get_portfolio(self, id):
        try:
            return Portfolio.objects.get(id=id)
        except Portfolio.DoesNotExist:
            raise Http404

    def get(self, request, id):
        portfolio = self.get_portfolio(id)
        serializer = PortfolioSerializer(portfolio)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        portfolio = self.get_portfolio(id)
        serializer = PortfolioSerializer(portfolio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        print(request.data)
        portfolio = self.get_portfolio(id)
        # serializer = PortfolioSerializer(portfolio)
        portfolio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

