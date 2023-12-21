import os.path

from bs4 import BeautifulSoup

from src.utils.get_html import get_html


def get_soup(url, cache_filename):
    try:
        if not os.path.isfile(cache_filename):
            print('No "' + cache_filename + '" found >> crawling url: ' + url + '...')
            soup = get_html(url)
            file_handle = open(cache_filename, 'w')
            file_handle.write(str(soup))
            print('HTML successfully cached in file "' + cache_filename + '" ✓')
        else:
            print('File "' + cache_filename + '" found >> cache used ✓')
            html_content = (open(cache_filename))
            soup = BeautifulSoup(html_content, 'html.parser')
    except:
        print('Problem with parsing HTML')
        quit()

    return soup
