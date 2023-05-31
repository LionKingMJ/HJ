from django.contrib import admin
from django.urls import path, include
import post.views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post', post.views.PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
