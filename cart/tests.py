from django.test import TestCase
from django.contrib.auth.models import User
from account.forms import UserRegisterForm

class CartTestsNotLoggedIn(TestCase):  
    '''
    testing cart page doesnt load when logged out
    (should return a 302 as the app should redirect to login page)
    '''
    def test_cart_page_load(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 302)

class CartTestsLoggedIn(TestCase):  

    # setting up logged in user
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
        self.client.post('/login/', self.credentials, follow=True)
    # testing cart page load when logged in
    def test_cart_page_load(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)

    def test_cart_page_templates_load(self):
        response = self.client.get('/cart/')
        self.assertTemplateUsed(response, "cart/cart.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "cart/includes/intro.html")
    