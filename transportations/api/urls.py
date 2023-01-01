from django.urls import path
from .views import TicketAddAPIView, TicketDetailAPIView

urlpatterns = [
    path('addticket/', TicketAddAPIView.as_view()),
    path('ticket/<int:pk>/', TicketDetailAPIView.as_view()),
]
