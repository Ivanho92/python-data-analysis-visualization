import json
import os

import config
from src.store.db import get_model

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
JAVASCRIPT_FILE_PATH = os.path.join(CURRENT_PATH, 'data.js')


def generate_js():
    data = get_model()
    file_handle = open(JAVASCRIPT_FILE_PATH, 'w')
    file_handle.write('const data = ' + json.dumps(data))
