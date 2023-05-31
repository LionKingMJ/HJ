from django.urls import path,include
from .views import *

urlpatterns = [
    path('lion/', lion, name='lion'),
    path('lion/<int:pk>',lionPosting, name="lionPosting"),
    path('lion/lionNewPost/',lionNewPost),
    path('lionEdit/<int:pk>',lionEdit, name='lionEdit'),
    path('lionUpdate/<int:pk>', lionUpdate, name='lionUpdate'),
    path('lionDel/<int:pk>', lionDel, name="lionDel"),
    path('lionForm/',lionForm, name='lionForm'),
    path('accounts/', include('allauth.urls')),
]
