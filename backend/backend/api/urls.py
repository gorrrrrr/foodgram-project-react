from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CustomUserCreateViewSet

# from .views import

app_name = 'api'

router = DefaultRouter()
router.register('users', CustomUserCreateViewSet, basename='user-create')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]
