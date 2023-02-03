from django.urls import path
from .views import NominationDetailView, NominationView

urlpatterns = [
    path('', NominationView.as_view()),
    path('<int:pk>', NominationDetailView.as_view())
]