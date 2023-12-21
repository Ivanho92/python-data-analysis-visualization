import os

from dotenv import load_dotenv

load_dotenv()

# Global variables
PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

URL = 'https://www.emcdda.europa.eu/data/stats2023/szr_en#displayTable:SZR-1-3-1'
TABLE_ID = 'SZR-1-3-1'
CACHE_FILENAME = 'page.html'
USE_CACHE = True

DB_CONTENT_NAME = 'content.sqlite'
DB_MODEL_NAME = 'model.sqlite'

API_ENDPOINT = 'https://maps.googleapis.com/maps/api/geocode/json'
MOCK_API_RESPONSE = False
