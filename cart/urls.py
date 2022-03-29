from django.urls import path
from cart import views


urlpatterns = [
    path('<int:pk>/', views.RetrieveUpdateDestroyCart.as_view()),
    path('', views.CreateAndListCart.as_view()),
]
