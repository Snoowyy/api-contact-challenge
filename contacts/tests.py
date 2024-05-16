from django.contrib.auth.models import User

from rest_framework.test import APITestCase

from contacts.models.contacts import Contact


class AuthTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            'testuser', 'text@example.com', password='testpassword')
        self.token = {}

    def test_authentication(self):
        response_token = self.client.post(
            '/token/', data={'username': self.user.username, 'password': 'testpassword'})
        self.token = response_token.json()
        self.assertEqual(response_token.status_code, 200)
        self.assertIn('access', self.token)
        self.assertIn('refresh', self.token)


class ContactTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            'testuser', 'text@example.com', password='testpassword')
        self.contact = Contact.objects.create(
            name='Prueba', mail='crismora1098@gmail.com', telephone='3022771375', user=self.user)
        self.token = {}

    def test_get_contacts(self):
        response_token = self.client.post(
            '/token/', data={'username': self.user.username, 'password': 'testpassword'})
        self.token = response_token.json()
        ##### VALIDATE TOKEN #####
        self.assertEqual(response_token.status_code, 200)
        self.assertIn('access', self.token)
        self.assertIn('refresh', self.token)
        ##### VALIDATE GET #####
        response = self.client.get(
            '/contacts/', **{'HTTP_AUTHORIZATION': f'Bearer {self.token["access"]}'})
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.contact.name, data[0]['name'])

    def test_post_contacts(self):
        response_token = self.client.post(
            '/token/', data={'username': self.user.username, 'password': 'testpassword'})
        self.token = response_token.json()
        ##### VALIDATE TOKEN #####
        self.assertEqual(response_token.status_code, 200)
        self.assertIn('access', self.token)
        self.assertIn('refresh', self.token)
        ##### VALIDATE GET #####
        response = self.client.post(
            '/contacts/create', data={
                'name': 'Prueba 2',
                'mail': 'example@test.com',
                'telephone': '3022771375',
            }, **{'HTTP_AUTHORIZATION': f'Bearer {self.token["access"]}'})
        data = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['name'], 'Prueba 2')

    def test_put_contacts(self):
        response_token = self.client.post(
            '/token/', data={'username': self.user.username, 'password': 'testpassword'})
        self.token = response_token.json()
        ##### VALIDATE TOKEN #####
        self.assertEqual(response_token.status_code, 200)
        self.assertIn('access', self.token)
        self.assertIn('refresh', self.token)
        ##### VALIDATE PUT #####
        self.assertEqual(self.contact.name, 'Prueba')
        response = self.client.put(
            f'/contacts/update/{self.contact.id}', data={
                'name': 'Prueba edit',
                'mail': 'example@test.com',
                'telephone': '3022771375',
            }, **{'HTTP_AUTHORIZATION': f'Bearer {self.token["access"]}'})
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], 'Prueba edit')

    def test_delete_contacts(self):
        response_token = self.client.post(
            '/token/', data={'username': self.user.username, 'password': 'testpassword'})
        self.token = response_token.json()
        ##### VALIDATE TOKEN #####
        self.assertEqual(response_token.status_code, 200)
        self.assertIn('access', self.token)
        self.assertIn('refresh', self.token)
        ##### VALIDATE DELETE #####
        self.assertEqual(self.contact.name, 'Prueba')
        response = self.client.delete(
            f'/contacts/delete/{self.contact.id}', **{'HTTP_AUTHORIZATION': f'Bearer {self.token["access"]}'})
        contact_deleted = Contact.objects.filter(id=self.contact.id).first()
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(contact_deleted)
