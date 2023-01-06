from django.urls import path, include


urlpatterns = [
    path('', include('payments.api.urls')),
]
