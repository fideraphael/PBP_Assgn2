from django.test import TestCase

class HomepageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/mywatchlist")
        self.assertEqual(response.status_code, 200)
# Create your tests here.
