def get_html(url, delay_time=1):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from bs4 import BeautifulSoup
    import time

    # Set up the headless browser
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the page
    driver.get(url)

    # Wait for a moment to let the JavaScript update the DOM
    time.sleep(delay_time)

    # Parse html
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')

    # Return parsed html
    driver.quit()
    return soup
