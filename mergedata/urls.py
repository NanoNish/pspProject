from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'data', views.DataViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('yep/', views.bruh),
]