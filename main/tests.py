from django.test import TestCase

# Create your tests here    
def test_indexpage(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
