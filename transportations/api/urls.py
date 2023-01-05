from django.urls import path
from .views import TicketsView

urlpatterns = [
    path('tickets/', TicketsView.as_view()),
]
