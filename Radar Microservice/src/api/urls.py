from django.urls import path
from . import views

urlpatterns = [
    # POST http://localhost:8001/api/attacks
    path("attacks", views.attack_detected)
]