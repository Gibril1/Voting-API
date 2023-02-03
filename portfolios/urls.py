from django.urls import path
from .views import PortfolioView, PortfolioDetailsView

urlpatterns = [
    path('<int:id>/', PortfolioView.as_view()),
    path('detail/<int:id>/', PortfolioDetailsView.as_view()),
]