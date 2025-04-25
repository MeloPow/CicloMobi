from django.urls import path
from .views import RegisterView, listar_usuarios

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('listar/', listar_usuarios),
]
