"""fang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from rest_framework.routers import DefaultRouter

from api import views

urlpatterns = [
    path('mobile_code/<str:tel>', views.mobile_code, name='mobile_code'),
    path('districts/', views.provinces, name='provinces'),
    path('districts/<int:pid>', views.districts, name='districts'),
    path('estates/<int:distid>', views.EstateView.as_view(), name='estates'),
]

router = DefaultRouter()
router.register('housetypes', views.HouseTypeViewSet)

urlpatterns += router.urls
