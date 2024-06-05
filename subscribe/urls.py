from django.urls import path
from . import views

app_name='subscribe'
urlpatterns = [

    path('', views.membership, name='index'),
    path('<int:pk>/', views.detail, name='subscribe_detail'),
    path('pay/', views.first_pay_process, name='payment'),
    path('paysuccess/', views.pay_success, name='paysuccess'),
    path('payfail/', views.pay_fail, name='payfail'),
    path('paycancel/', views.pay_cancel, name='paycancel'),    
    
]