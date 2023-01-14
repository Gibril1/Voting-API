from django.urls import path
from .views.nominations import (
    NominationView, 
    NominationDetailView, 
    ApprovalView, 
    VotingView
)

urlpatterns = [
    path('', NominationView.as_view()),
    path('<int:id>/', NominationDetailView.as_view()),
    path('approve/<int:id>', ApprovalView.as_view()),
    path('vote/<int:id>', VotingView.as_view())
]