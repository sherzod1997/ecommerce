from django.urls import path
from .views import CustomerDetail, ProductList,ProductDetail,CustomerList,OrderList,OrderDetail

urlpatterns=[
    path('<int:pk>',ProductDetail.as_view()),
    path('',ProductList.as_view()),
    path('customer/',CustomerList.as_view()),
    path('customer/<int:pk>/',CustomerDetail.as_view()),
    path('order/',OrderList.as_view()),
    path('order/<int:pk>/',OrderDetail.as_view()),
]