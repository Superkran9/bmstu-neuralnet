"""
URL configuration for neuralnet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
'''
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bert_classifier/', include('bert_classifier.urls')),  # Маршруты приложения bert_classifier
    path('', include('bert_classifier.urls')),  # Главная страница перенаправляется на bert_classifier
]
'''

from django.contrib import admin
from django.urls import include, path
from .views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('bert_classifier/', include('bert_classifier.urls')),
    path('dialog_bot/', include('dialog_bot.urls')),
    path('image_classification/', include('image_classification.urls')),
]

