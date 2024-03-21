from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class TestListCreateTodos(APITestCase):

    def authenticate(self):
        self.client.post(reverse("register"),{
            'username':"username",'email':"email@gmail.com",'password':'password'})
        response= self.client.post(
            reverse('login'), {"email":"email@gmail.com", "password": "password"}
        )
        self.client.credentials(HTTP_AUTHORIZATION= f"Bearer {response.data['token']}")

    def test_should_not_create_todo_with_no_auth(self):
        sample_todo = {'title':'Hello', 'desc': 'Test'}
        response = self.client.post(reverse('todos'), sample_todo)
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)


    def test_should_create_todo(self):
        # self.authenticate()
        sample_todo = {'title':'Hello', 'desc': 'Test'}
        response = self.client.post(reverse('todos'), sample_todo)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
