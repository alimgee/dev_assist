from django.test import TestCase
from users.forms import UserRegisterForm


class UserTests(TestCase):
    # testing registration form accepts valid data
    def test_forms(self):
        form_data = {'username': 'djangotest',
        'email': 'test@test.com',
        'password1': 'm1234rthq',
        'password2': 'm1234rthq',}
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())
