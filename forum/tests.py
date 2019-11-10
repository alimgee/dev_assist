from django.test import TestCase
from forum.views import PostListView


# Test to check the forum
class TestPost(TestCase):
    # testing loading of forum landing page
    def test_forum_landing_page(self):
        response = self.client.get('/community/')
        self.assertEqual(response.status_code, 200)
)
