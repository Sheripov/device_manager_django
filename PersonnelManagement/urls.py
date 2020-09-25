"""PersonnelManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from API import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'team', views.TeamViewSet)
router.register(r'buyer', views.BuyerViewSet)
router.register(r'devicetype', views.DeviceTypeViewSet)
router.register(r'device', views.DeviceViewSet)
router.register(r'assignment', views.AssignmentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('management.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
