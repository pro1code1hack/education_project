from django.urls import path
from . import views

urlpatterns = [
    path('distant/', views.distant_learning, name='distant_learning'),
    path('distant/<int:grade>/', views.distant_learning, name='distant_learning'),
]