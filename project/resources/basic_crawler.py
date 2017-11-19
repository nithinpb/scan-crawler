import logging
import requests
from bs4 import BeautifulSoup

class BasicCrawler(object):

    crawl_map = {}
    links_list = list()
    seed, depth = None, 0

    def __init__(self, seed, depth): 
        self.crawl_map = {
            "seed": seed,
            "depth": depth,
            "contents": []
        }
        self.seed = seed
        self.depth = depth

    def start_crawl(self, seed=None, depth=None): 
        seed = seed or self.seed
        depth = depth or self.depth

        self.crawl(seed, depth)
        return self.crawl_map

    def format_url(self, root, url):

        def base(u):
            u = u.split('?')[0].rstrip('/')
            return u

        root = base(root)

        if url == "/":
            return None
        elif url.startswith("http://"):
            return base(url)
        elif url.startswith("/"):
            return root + url


    def crawl(self, seed, depth):
        print "Crawling {seed} at {depth}".format(seed=seed, depth=depth)

        response = requests.get(seed)
        soup = BeautifulSoup(response.content, "html.parser")

        imgs = []
        for img in soup.find_all('img', src=True):
            img_src = self.format_url(seed, img['src'])

            if img_src and img_src not in imgs:
                imgs.append(img_src)

        result = {
            'link': seed,
            'images': imgs
        }
        self.crawl_map["contents"].append(result)

        if depth:
            for anchor in soup.find_all('a', href=True):
                sub_link = self.format_url(seed, anchor['href'])

                if sub_link and sub_link not in self.links_list and len(self.links_list) < 4:
                    self.links_list.append(sub_link)
                    self.crawl(sub_link, depth - 1)