from django.urls import path, include


urlpatterns = [
    path('', include('residences.api.urls')),
]

