from django.test import TestCase
from django.contrib.auth.models import User
from account.forms import UserRegisterForm


class CartTestsLoggedIn(TestCase):

    # setting up logged in user
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
        self.client.post('/login/', self.credentials, follow=True)

    # testing checkout page load when logged in
    def test_cart_page_load(self):
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
