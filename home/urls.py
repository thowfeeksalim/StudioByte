from django.urls import path,include
from. import views

urlpatterns = [
    path('', views.index, name='home'),
    path('ABOUT/', views.ABOUT, name='about'),
    path('BOOKING/', views.BOOKING ,name='booking'),
    path('OCCATIONS', views.OCCATIONS ,name='occations'), 
    path('CONTACT', views.CONTACT, name='contact'), 
    path('DEPARTMENT', views.DEPARTMENT, name='department'), 
    
]