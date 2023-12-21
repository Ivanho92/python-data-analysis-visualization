import os

import config
from src.crawler.parser import parse_data
from src.crawler.soup import get_soup
from src.store.db import store_content


def crawl():
    # 1) Crawl data from the internet
    try:
        soup = get_soup(config.URL, os.path.join(config.PROJECT_ROOT_PATH, config.CACHE_FILENAME))
    except Exception as error:
        print('ERROR >> Problem with scrapping\n', error)
        quit()

    # 2) Parse data
    try:
        data = parse_data(soup, config.TABLE_ID)
    except Exception as error:
        print('ERROR >> Problem with parsing\n', error)
        quit()

    # 3) Store to db
    store_content(data)
