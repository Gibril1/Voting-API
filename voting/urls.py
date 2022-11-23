from django.urls import path
from .views import NominationView, NominationDetailView

urlpatterns = [
    path('', NominationView.as_view()),
    path('<int:id>/', NominationDetailView.as_view())
]