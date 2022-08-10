"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from .views import ItView, AddItView, UpdateItView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', AddItView.as_view(), name='it'),
    path('tasks', ItView.as_view(), name='it_tasks'),
    path('tasks/edit/<int:pk>', UpdateItView.as_view(), name='it_update'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
