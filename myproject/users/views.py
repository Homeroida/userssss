from django.contrib.auth.models import Group
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer, CustomTokenObtainPairSerializer

class RegisterSellerView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save(is_seller=True)
        group, _ = Group.objects.get_or_create(name='Seller')
        user.groups.add(group)

class RegisterBuyerView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save(is_seller=False)
        group, _ = Group.objects.get_or_create(name='Buyer')
        user.groups.add(group)

class SellerTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class BuyerTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
