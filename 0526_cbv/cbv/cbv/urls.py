from django.contrib import admin
from django.urls import path
import cbvtest.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', cbvtest.views.test, name='test'),
]
