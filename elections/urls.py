from django.urls import path

from .views import (
    ListElectionsView,
    ElectionDetailView,
    CreateElectionView
)

urlpatterns = [
    path('', ListElectionsView.as_view()),
    path('create/', CreateElectionView.as_view()),
    path('<int:pk>/', ElectionDetailView.as_view()),
]