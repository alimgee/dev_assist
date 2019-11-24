from django.test import TestCase
from account.forms import UserRegisterForm
from django.contrib.auth.models import User


class UserTests(TestCase):  

    # testing load of pages in account app
    def test_register_page_load(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_login_page_load(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
    
    def test_logout_page_load(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 200)

    # testing log in function
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)
    
    # testing registration form accepts valid data
    def test_forms(self):
        form_data = {'username': 'djangotest',
        'email': 'test@test.com',
        'password1': 'm1234rthq',
        'password2': 'm1234rthq',}
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())
