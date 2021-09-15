from django.db.models import fields
from rest_framework import serializers
from store.models import Product,Customer,Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('id','name','price','digital','image')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=('id','user','name','email') 

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=('__all__')               