from rest_framework  import serializers
from .models import Product

class ProductSerialize(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','name','details','price']