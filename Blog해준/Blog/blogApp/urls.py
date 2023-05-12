from django.urls import path
from .views import *

# 이미지를 업로드하자
# from django.conf.urls.static import static
# from django.conf import settings

urlpatterns = [
    path('lion/', lion, name='lion'),
    path('lion/<int:pk>',lionPosting, name="lionPosting"),
    path('lion/lionNewPost/',lionNewPost),
    path('lionEdit/<int:pk>',lionEdit, name='lionEdit')
        #id값 받아야하는지 checks
]

# 이미지 URL 설정
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)