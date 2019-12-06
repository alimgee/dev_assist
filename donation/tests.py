from django.test import TestCase


class UserTests(TestCase):

    # testing load of donate page
    def test_donate_page_load(self):
        response = self.client.get('/donate/')
        self.assertEqual(response.status_code, 200)

    # testing load of relevant templates to donate page
    def test_donate_page_templates_load(self):
        response = self.client.get('/donate/')
        self.assertTemplateUsed(response, "donation/donation.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "donation/includes/intro.html")
