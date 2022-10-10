from django.urls import path
from . import views

urlpatterns = [
    # path('lesson/', views.lesson_list, name='display_lessons'),
    # path('lesson/<str:grade>', views.lesson_list, name='lesson'),
    path('lessons/', views.LessonListView.as_view(), name='display_lessons'),
    path('lessons/<str:grade>', views.LessonListView.as_view(), name='lessons'),
    path('lesson/<int:pk>/', views.get_lesson, name='lesson'),
    path('/', views.main_page, name='batya_profile')
]
