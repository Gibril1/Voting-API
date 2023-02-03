from django.urls import path

from .views import (
    ElectionView,
    ElectionDetailView
)

urlpatterns = [
    path('', ElectionView.as_view()),
    path('<int:pk>/', ElectionDetailView.as_view()),
]