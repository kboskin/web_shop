from rest_framework import serializers

from cart.serializers import OrderSerializer
from customer.serializers import UserSerializer


class PaymentLogSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    user = UserSerializer()

    class Meta:
        fields = ['id', 'address', 'type', 'status', 'order', 'user', 'date', 'request_data', 'response_data']
