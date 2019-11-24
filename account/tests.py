from django.test import TestCase
from account.forms import UserRegisterForm


class UserTests(TestCase):  

    # testing load of pages in account app
    def test_register_page_load(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_login_page_load(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
    
    def test_logoit_page_load(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 200)
    
    # testing registration form accepts valid data
    def test_forms(self):
        form_data = {'username': 'djangotest',
        'email': 'test@test.com',
        'password1': 'm1234rthq',
        'password2': 'm1234rthq',}
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())
