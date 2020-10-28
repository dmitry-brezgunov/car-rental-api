from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import UserCreate, UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserCreate.as_view()),
    path('token/', views.obtain_auth_token),
]
