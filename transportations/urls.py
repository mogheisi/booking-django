from django.urls import path, include


urlpatterns = [
    path('', include('transportations.api.urls')),
]
