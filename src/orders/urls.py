from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('create_order/', views.create_order, name='create_order'),
    path('orders/', views.order_list, name='order_list'),
    path('bill/<int:pk>/', views.generate_bill, name='generate_bill'),
    path('accounts/login/', views.login_view, name='login'),  
    path('logout/', views.logout_view, name='logout'),  # Logout page
    path('mark_as_paid/<int:pk>/', views.mark_as_paid, name='mark_as_paid'),
]
