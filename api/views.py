from django.db.models import query
from rest_framework import generics
from store.models import Product,Customer,Order,OrderItem,ShippingAddress
from .serializers import ProductSerializer,CustomerSerializer,OrderSerializer

class ProductList(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class CustomerList(generics.ListAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer 

class CustomerDetail(generics.RetrieveAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

class OrderList(generics.ListAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer 

class OrderDetail(generics.RetrieveAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer      


