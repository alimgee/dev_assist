from django.test import TestCase
from django.contrib.auth.models import User
from account.forms import UserRegisterForm


class CheckoutTestsLoggedOut(TestCase):
    def test_checkout_page_load(self):
        '''
        function to check that users cannot load
        checkout page if not logged in
        '''
        response = self.client.get('/checkout/')
        # page should redirect if not logged in
        self.assertEqual(response.status_code, 302)


class CheckoutTestsLoggedIn(TestCase):
    # setting up logged in user
    def setUp(self):
        '''
        function to check that users can load
        checkout page if logged in
        '''
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
        self.client.post('/login/', self.credentials, follow=True)

    # testing checkout page load when logged in
    def test_checkout_page_load(self):
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)

    # testing checkout templates load as expected
    def test_checkout_page_templates_load(self):
        response = self.client.get('/checkout/')
        self.assertTemplateUsed(response, "checkout/checkout.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "checkout/includes/intro.html")
