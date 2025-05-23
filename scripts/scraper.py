from urllib.parse import urljoin, urlencode
import undetected_chromedriver as uc
import time 

# undetected_chromedriver expects Intel (x86_64) ChromeDriver, but I am running  Apple Silicon (arm64)
# need to:
# 1. brew install chromedriver
# 2. find chromedriver path (usually: /opt/homebrew/bin/chromedriver) using `which chromedriver`
# 3. Provide this to undetected_chromedriver.Chrome()
# 
# Had to do some funky stuff to get chromedriver to work


CHROMEDRIVER_PATH = '/Users/danstock/bin/chromedriver'

INDEED_URL = 'https://uk.indeed.com/'

def construct_url(params:dict):
    if params is None:
        raise TypeError('Expected params to be a dict, but got None.')
    
    if 'q' not in params:
        raise Exception('q key required in search parameters')
    
    # Encode strings into url safe format
    base = INDEED_URL
    path = 'jobs?' + urlencode(params)
    return urljoin(base, path)

    
def main():
    search_params = {
        'q': 'machine learning',
        'l': 'london'
    }

    url = construct_url(search_params)


    driver = uc.Chrome(driver_executable_path=CHROMEDRIVER_PATH, headless=False)
    driver.get(url)
    print(driver.page_source[:1000])
    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    main()