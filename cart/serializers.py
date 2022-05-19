from rest_framework import serializers

from cart.models import Cart, CartItem, Order, OrderItem
from customer.serializers import UserSerializer


class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'created_date']


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'qty']


class OrderSerializer(serializers.ModelSerializer):
    cart = CartSerializer()

    class Meta:
        model = Order
        fields = ['id', 'cart', 'delivery_type', 'delivery_address', 'total_items_count',
                  'order_status', 'last_payment_id', 'products', 'user', 'order_date']


class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'product_qty']
