import os.path

from bs4 import BeautifulSoup

import config
from src.utils.get_html import get_html

PAGE_PATH = os.path.join(config.PROJECT_ROOT_PATH, 'src', 'crawler', config.CACHE_FILENAME)


def fetch_and_cache():
    soup = get_html(config.URL)
    file_handle = open(PAGE_PATH, 'w')
    file_handle.write(str(soup))
    return soup


def get_soup(use_cache=True):
    try:
        cache_page_found = os.path.isfile(PAGE_PATH)
        if not use_cache or not cache_page_found:
            crawl_reason = 'Ignore cache' if not use_cache else 'No "' + config.CACHE_FILENAME + '" found'
            print(crawl_reason + ' >> crawling url: ' + config.URL + '...')
            soup = fetch_and_cache()
            print('HTML successfully cached in file "' + config.CACHE_FILENAME + '" ✓')
        else:
            print('File "' + config.CACHE_FILENAME + '" found >> cache used ✓')
            html_content = (open(PAGE_PATH))
            soup = BeautifulSoup(html_content, 'html.parser')
        return soup
    except:
        print('Problem with parsing HTML')
        quit()
