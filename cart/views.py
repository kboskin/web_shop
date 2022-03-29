from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

# Create your views here.
from cart.models import Cart
from cart.serializers import CartSerializer
from rest_framework.permissions import IsAdminUser


class CreateAndListCart(ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class RetrieveUpdateDestroyCart(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
