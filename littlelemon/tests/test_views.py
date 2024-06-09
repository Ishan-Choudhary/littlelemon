from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

class MenuViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.item1 = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.item2 = Menu.objects.create(Title="Cake", Price=100, Inventory=150)
        self.item3 = Menu.objects.create(Title="Sundae", Price=50, Inventory=10)
        self.item4 = Menu.objects.create(Title="Chocolate", Price=90, Inventory=200)
    
    def test_getall(self):
        response = self.client.get(reverse('menu-list'))  # Adjust 'menu-list' to your URL pattern name
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
