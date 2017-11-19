import os

VERSION = "0.1.0"
PORT = os.getenv('PORT', 5000)
DEBUG = bool(os.getenv('DEBUG', True))
JSON_DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"