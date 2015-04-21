from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http import HttpRequest

# Create your tests here.

class HomePageTest(TestCase):

	"""
	Added a class that inherits Django's custom unittesting class called
		TestCase. It should handle all of the same tests as unittest.
	"""

	def test_root_url_resolves_to_home_page_view(self):
		
		"""
		The method tests to see if the resolve function is equivalent to
			the home_page we programmed in lists.views. resolve is matched
			against the superlists/superlists/urls.py file to see if your
			regex hits on a real site.

		Args:
			found (<class 'django.core.urlresolvers.ResolverMatch'>): This
				attempts to store the results of django's built in resolve()
				method. This method takes your base url and adds whatever
				you put onto the end of it.
		"""
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	
	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		self.assertTrue(response.content.startswith(b'<html>'))
		self.assertIn(b"SOME TEXT", response.content)
		self.assertTrue(response.content.endswith(b'</html>'))



	#print(test_root_url_resolves_to_home_page_view.__doc__)
