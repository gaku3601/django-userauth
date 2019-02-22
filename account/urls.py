from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('jwt-token/', obtain_jwt_token),
    path('', include(router.urls)),
]
