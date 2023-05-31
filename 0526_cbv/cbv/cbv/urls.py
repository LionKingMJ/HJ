from django.contrib import admin
from django.urls import path
import cbvtest.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cbvtest.views.BlogView.as_view(), name='list'),
    path('newblog/', cbvtest.views.BlogCreate.as_view(), name = 'new'),
    path('detail/<int:pk>', cbvtest.views.BlogDetail.as_view(), name = 'detail'),
    path('update/<int:pk>', cbvtest.views.BlogUpdate.as_view(), name = 'change'),
    path('delete/<int:pk>', cbvtest.views.BlogDelete.as_view(), name = 'del'),
]
