import logging
import unittest

from requests import ConnectionError
from project.core import ApplicationError
from project.resources.basic_crawler import BasicCrawler

class CrawlerTest(unittest.TestCase):
    """Tests different methods of the BasicCrawler"""

    def _create_fixtures(self): 
        self.seed = "http://www.skidata.com"
        self.depth = 0
        self.crawler = BasicCrawler(self.seed, self.depth)

    def setUp(self):
        super(CrawlerTest, self).setUp()
        self._create_fixtures()

    def tearDown(self):
        super(CrawlerTest, self).tearDown()
        
    def test_format_url(self):
        self.assertEqual( self.crawler.format_url(self.crawler.seed, "/google"),
            self.seed + "/google")
        self.assertEqual( self.crawler.format_url(self.crawler.seed, "/"),
            self.seed)
        self.assertEqual( self.crawler.format_url("hello", self.crawler.seed),
            self.seed)
        self.assertEqual( self.crawler.format_url("hello", "https://dev.to"),
            "https://dev.to")
        self.assertEqual( self.crawler.format_url("hello", "https://dev.to?google=facebook"),
            "https://dev.to")        

    def test_unreachable_seed(self): 
        try:
            self.crawler.start_crawl("http://localhost", 0)
        except ConnectionError:
            pass
        except Exception as e:
           self.fail('Unexpected exception raised:' + str(e))
        else:
           self.fail('ExpectedException not raised')

    def test_invalid_seed(self):
        try:
            BasicCrawler(None, 1)
        except ApplicationError:
            pass
        except Exception as e:
           self.fail('Unexpected exception raised:' + str(e))
        else:
           self.fail('ExpectedException not raised')

    def test_invalid_depth(self): 
        try:
            BasicCrawler(self.seed, None)
        except ApplicationError:
            pass
        except Exception as e:
           self.fail('Unexpected exception raised:' + str(e))
        else:
           self.fail('ExpectedException not raised')

    def test_start_crawl(self):
        self.assertIsNotNone( self.crawler.start_crawl() )

