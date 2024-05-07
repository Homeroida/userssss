from django.urls import path
from .views import RegisterSellerView, RegisterBuyerView, SellerTokenObtainPairView, BuyerTokenObtainPairView

urlpatterns = [
    path('register/seller/', RegisterSellerView.as_view(), name='register_seller'),
    path('register/buyer/', RegisterBuyerView.as_view(), name='register_buyer'),
    path('login/seller/', SellerTokenObtainPairView.as_view(), name='seller_login'),
    path('login/buyer/', BuyerTokenObtainPairView.as_view(), name='buyer_login'),

]
