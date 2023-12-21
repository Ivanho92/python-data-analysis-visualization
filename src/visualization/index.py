import json
import os

import config
from src.store.db import get_model


def generate_js():
    data = get_model()
    file_handle = open(os.path.join(config.PROJECT_ROOT_PATH, 'data.js'), 'w')
    file_handle.write('const data = ' + json.dumps(data))
