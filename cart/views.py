from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cart.models import Cart
from cart.serializers import CartSerializer


class CreateAndListCart(ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Cart.objects.all()

    def create(self, request, *args, **kwargs):
        request.data['customer'] = self.get_serializer_context()['request'].user
        cart_serializer = self.get_serializer(data=request.data)
        if cart_serializer.is_valid(raise_exception=True):
            cart_serializer.save()
            return Response(status=status.HTTP_201_CREATED)


class RetrieveUpdateDestroyCart(RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer

    def get_object(self):
        cart_id = self.kwargs.get('cartId')
        return get_object_or_404(self.get_queryset(), pk=cart_id)
