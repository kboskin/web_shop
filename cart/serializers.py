from rest_framework import serializers

from cart.models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'customer', 'created_date']


class BookedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'cart', 'product', 'qty', 'customer']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'cart', 'delivery_type', 'delivery_address', 'total_items_count',
                  'order_status', 'last_payment_id', 'products', 'customer', 'order_date']
