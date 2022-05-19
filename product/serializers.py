from rest_framework import serializers

from catalogue.serializers import CategorySerializer
from customer.serializers import UserSerializer


class DistributorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name', 'address', 'phone']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    distributor = DistributorSerializer()

    class Meta:
        fields = ['id', 'name', 'description', 'price', 'category', 'category', 'distributor', 'amount']


class ImageSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        fields = ['id', 'image_big', 'image_small', 'product']


class Feedback(serializers.ModelSerializer):
    product = ProductSerializer()
    user = UserSerializer()

    class Meta:
        fields = ['id', 'product', 'user', 'date', 'message']