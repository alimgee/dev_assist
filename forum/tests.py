from django.test import TestCase


# Tests to check the forum
class TestForum(TestCase):
    # testing loading of forum landing page
    def test_forum_landing_page(self):
        response = self.client.get('/community/')
        self.assertEqual(response.status_code, 200)

    # testing load of relevant templates to community page
    def test_forum_page_templates_load(self):
        response = self.client.get('/community/')
        self.assertTemplateUsed(response, "forum/forum_list.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "forum/includes/intro.html")   
