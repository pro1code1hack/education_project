from django.urls import path
from . import views

urlpatterns = [
    path('distant_lessons/<int:course>/', views.distant_learning_course, name='Все дистанционные уроки для курса'),
    path('distant_lessons/<int:course>/<int:pk>/', views.distant_learning_single, name='Одиночный дистанционный урок'),
    path('distant_topics/<int:course>/', views.distant_learning_all_topics_course, name='Список тем для курса'),
]