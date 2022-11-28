from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.

class SancksTest(SimpleTestCase):

    def test_index_status(self):

        url=reverse('index')
        
        response =self.client.get(url)
        self.assertEqual(response.status_code,200)
      
    def test_about_status(self):

        url=reverse('about')
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_index_template(self):

        url=reverse('index')
        
        response =self.client.get(url)
        self.assertTemplateUsed(response,'index.html')
      
    def test_about_template(self):

        url=reverse('about')
        response=self.client.get(url)
        self.assertTemplateUsed(response,'about.html')
        
      

    