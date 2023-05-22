from django.contrib import admin
from django.urls import path, include
import blogApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogApp.urls')), #view와 url을 연결시켜준다, main에서의 urls을 불러온다
]
