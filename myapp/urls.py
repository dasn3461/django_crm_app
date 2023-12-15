from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('logout/', views.user_logout, name="logout"),
    path('register/', views.Register_User, name="register"),
    path('record/<int:pk>/', views.custoer_record, name="record"),
    path('delete_record/<int:pk>/', views.delete_record, name="delete"),
    path('update_record/<int:pk>/', views.update_record, name="update"),
    path('add_record/', views.add_record, name="addrecord"),
    
]
