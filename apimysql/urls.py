from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('nhanvien', views.NhanVienViewSet, basename='nhanvien')
router.register('phongban', views.PhongBanViewSet, basename='phongban')




urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include(router.urls)),
    
    
]