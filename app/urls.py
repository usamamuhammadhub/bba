from django.urls import path
from app import views
urlpatterns = [
    path('', views.home,name='home'),
   
    path('send_mail1/', views.send_mail1, name='send_mail1'),
  
]
