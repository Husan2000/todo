from django.urls import path
from .views import index, single


urlpatterns = [
    path('', index, name='index'),
    path('edit/<int:pk>/', single, name='single'),
]
