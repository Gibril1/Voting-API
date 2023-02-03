from django.urls import path



from .views import (
    ApprovalView,
    VotingView,
    ContestantsView
)

urlpatterns = [
    path('approve/<int:id>/', ApprovalView.as_view()),
    path('vote/<int:id>/', VotingView.as_view()), 
    path('contestants/', ContestantsView.as_view() )
    

]