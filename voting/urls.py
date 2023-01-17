from django.urls import path
from .views.nominations import (
    NominationView, 
    NominationDetailView, 
)
from .views.votings import (
    ApprovalView,
    VotingView,
    ContestantsView
)
from .views.portfolios import (
    PortfolioDetailsView,
    PortfolioView
)

from .views.elections import (
    ElectionView,
    ElectionDetailView
)

urlpatterns = [
    path('', NominationView.as_view()),
    path('<int:id>/', NominationDetailView.as_view()),
    path('approve/<int:id>', ApprovalView.as_view()),
    path('vote/<int:id>', VotingView.as_view()), 
    path('contestants/', ContestantsView.as_view() ),
    path('portfolio/', PortfolioView.as_view()),
    path('portfolio/<int:id>', PortfolioDetailsView.as_view()),
    path('election/', ElectionView.as_view()),
    path('election/<int:id>', ElectionDetailView.as_view()),

]