from django.urls import path
from . import views, apis_views


app_name = 'cats'

urlpatterns = [
    
    path('', views.CatList.as_view(), name='cat_list'),
    
    path('create/', views.CatCreate.as_view(), name='cat_create'),
    
    path('update/<int:pk>/', views.CatUpdate.as_view(), name='cat_update'),
    
    path('delete/<int:pk>/', views.CatDelete.as_view(), name='cat_delete'),
    
    path('detail/<int:pk>/', views.CatDetail.as_view(), name='cat_detail'),
    
    # APIS:
    
    path('api_cat_list/', apis_views.ApiCatList, name='cat_api_list'),
    
    path('api_cat_delete/<int:pk>/', apis_views.ApiCatDelete, name='cat_api_delete'),
    
]