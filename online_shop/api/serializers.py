from rest_framework import serializers
from store_app.models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = '__all__'


