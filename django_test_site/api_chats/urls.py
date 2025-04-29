from django.urls import path
from . import views 

app_name = 'api_chats'

urlpatterns = [
    
    path('chats_list/', views.ChatsListApi, name='chats_list'),

    
]