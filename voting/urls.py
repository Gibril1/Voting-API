from django.urls import path
from .views import NominationView, NominationDetailView, ApprovalView

urlpatterns = [
    path('', NominationView.as_view()),
    path('<int:id>/', NominationDetailView.as_view()),
    path('vote/<int:id>', ApprovalView.as_view())
]