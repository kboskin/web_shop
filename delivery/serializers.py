from rest_framework import serializers

from cart.serializers import OrderSerializer
from customer.serializers import UserSerializer


class DeliveryLogSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    user = UserSerializer()

    class Meta:
        fields = ['id', 'order', 'user', 'amount', 'type', 'status', 'date', 'request_data', 'response_data']
