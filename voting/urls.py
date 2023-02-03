from django.urls import path


from .views.portfolios import (
    PortfolioDetailsView,
    PortfolioView
)
from .views.nominations import (
    NominationView, 
    NominationDetailView, 
)
from .views.votings import (
    ApprovalView,
    VotingView,
    ContestantsView
)

urlpatterns = [
    path('<int:id>/', NominationView.as_view()),
    path('nomination/<int:id>/', NominationDetailView.as_view()),
    path('approve/<int:id>/', ApprovalView.as_view()),
    path('vote/<int:id>/', VotingView.as_view()), 
    path('contestants/', ContestantsView.as_view() ),
    path('portfolio/<int:id>', PortfolioView.as_view()),
    path('portfolio-detail/<int:id>/', PortfolioDetailsView.as_view()),
    

]