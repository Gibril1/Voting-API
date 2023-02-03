from django.urls import path
from .views import ListPortfoliosView, PortfolioDetailsView,  CreatePortfolioView

urlpatterns = [
    path('', ListPortfoliosView.as_view()),
    path('create/<int:id>', CreatePortfolioView.as_view()),
    path('detail/<int:id>/', PortfolioDetailsView.as_view()),
]