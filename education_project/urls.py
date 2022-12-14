"""education_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from .views import homework, render404, main_page, homework_single, textbooks, methodical_work
from django.conf.urls.static import static
# from .views import main_page
# from .views import homework
# from .views import homework_single


# from templates import main

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('lessons.urls')),
    # path('', include('distant_learning.urls')),
    path('404/', render404),
    path('', main_page),
    path('homework', homework),
    path('homework/1', homework_single),
    path('textbooks', textbooks),
    path('methodical_work', methodical_work),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
