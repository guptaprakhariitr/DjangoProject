from django.urls import path
from .views import api_detail,api_create,api_delete,api_update

urlpatterns = [
    path('',api_detail,name='api-blog-home'),
    path('<int:pk>/update',api_update,name='api-blog-update'),
    path('<int:pk>/delete',api_delete,name='api-blog-delete'),
    path('create',api_create,name='api-blog-create') ,   
]