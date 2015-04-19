from selenium import webdriver
import time
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		time.sleep(4)
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		#User goes to a new site to check it out;
		self.browser.get("http://localhost:8000")

		#Site has a new title : "To-Do" for To-Do Lists
		self.assertIn("To-Do", self.browser.title)
		self.fail("finish the test")

		#User is invited to enter a To do item:


		#User enters buy peacock feathers into the text field:


		#When the user hits enter, the page updates and now the page lists:
		#"1: Buy peackock feathers" as an item in the to-do list


		#There is still a textbox inviting the user to enter another item.
		#The user enters "use said peacock feathers to make a pen"


		#The page updates again and shows both items


		#The user wishes to save the list. The page has generated a specific URL for her


		#The user visits the custom url and her list is still there


if __name__ == '__main__':
	unittest.main(warnings='ignore')