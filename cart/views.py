from django.http import Http404
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from cart.models import Cart
from cart.serializers import CartSerializer
from rest_framework.permissions import IsAdminUser


class CartMixin:
    def get_cart_by_id(self, request):
        return list(filter(lambda item: item != '', request.path.split('/')))[-1]


class CreateAndListCart(CartMixin, ListCreateAPIView):
    serializer_class = CartSerializer

    def get_object(self):
        cart_id = self.get_cart_by_id(self.request)
        if cart_id in self.get_queryset():
            return self.get_queryset().get(pk=cart_id)
        else:
            raise Http404

    def get_queryset(self):
        return Cart.objects.all()


class RetrieveUpdateDestroyCart(CartMixin, RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer

    def get_object(self):

        cart_id = self.get_cart_by_id(self.request)
        if cart_id in self.get_queryset():
            return self.get_queryset().get(pk=cart_id)
        else:
            raise Http404

    def get_queryset(self):
        return Cart.objects.all()
