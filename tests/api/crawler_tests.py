from . import ProjectApiTestCase

class CrawlerApiTestCase(ProjectApiTestCase):
	"""Test if the APIs respond with JSON"""
	
    def test_get_version(self):
        r = self.send_request('/crawler/')
        self.assertOkJson(r)

    def test_get_sample(self):
        r = self.send_request('/crawler/sample')
        self.assertOkJson(r)