from django.urls import path
from . import views

urlpatterns = [
    # path('lesson/', views.lesson_list, name='display_lessons'),
    # path('lesson/<str:grade>', views.lesson_list, name='lesson'),
    path('lesson/', views.LessonListView.as_view(), name='display_lessons'),
    path('lesson/<str:grade>', views.LessonListView.as_view(), name='lesson'),
]
