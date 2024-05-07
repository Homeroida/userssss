# users/tests.py
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework.test import APITestCase
from rest_framework import status

User = get_user_model()

class UserRegistrationAndLoginTest(APITestCase):
    def setUp(self):
        # Ensure the Seller and Buyer groups exist
        Group.objects.get_or_create(name='Seller')
        Group.objects.get_or_create(name='Buyer')

    def test_seller_registration(self):
        url = reverse('register_seller')
        data = {
            'username': 'seller',
            'email': 'seller@example.com',
            'password': 'password123',
            'is_seller': True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='seller').exists())
        user = User.objects.get(username='seller')
        self.assertTrue(user.groups.filter(name='Seller').exists())

    def test_buyer_registration(self):
        url = reverse('register_buyer')
        data = {
            'username': 'buyer',
            'email': 'buyer@example.com',
            'password': 'password123',
            'is_seller': False
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='buyer').exists())
        user = User.objects.get(username='buyer')
        self.assertTrue(user.groups.filter(name='Buyer').exists())

    def test_seller_login_and_token(self):
        self.test_seller_registration()  # First, ensure a seller is registered
        url = reverse('seller_login')
        data = {'username': 'seller', 'password': 'password123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_buyer_login_and_token(self):
        self.test_buyer_registration()  # First, ensure a buyer is registered
        url = reverse('buyer_login')
        data = {'username': 'buyer', 'password': 'password123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
