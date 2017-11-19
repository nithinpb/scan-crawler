from flask import Blueprint
from flask import request

import json
from os import path
from ...resources.basic_crawler import BasicCrawler
from ...settings import VERSION, DEBUG
from . import route

bp = Blueprint('crawler', __name__, url_prefix='/crawler')

@route(bp, '/')
def version():
    return {'version': VERSION}

@route(bp, '/sample')
def sample(): 
    file = path.join(path.dirname(__file__), 'sample.json')
    return json.load(open(file)) if DEBUG else {}

@route(bp, '/crawl/')
def execute():

    def _validate_seed( seed ): 
        if seed.index('http://') == 0 or seed.index('https://') == 0:
            return seed

        return "http://" + seed

    def _validate_depth( depth ): 
        if not depth.isdigit():
            return 1

        return int(depth)
        
    seed = _validate_seed( request.args.get('seed') )
    depth = _validate_depth( request.args.get('depth') )
    return BasicCrawler(seed, depth).start_crawl()