from django.urls import path
from cart import views


urlpatterns = [
    path('<int:cartId>/', views.RetrieveUpdateDestroyCart.as_view()),
    path('', views.CreateAndListCart.as_view()),
]
