# Making a selenium bot to play youtube videos.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options



options = Options()
options.add_experimental_option("detach", True)
options.add_extension('uBlockOrigin.crx')
options.add_argument = ('--user-data-dir=C:/Users/dedsec995/AppData/Local/Google/Chrome/User Data')
driver = webdriver.Chrome(options=options)
driver.get("https://youtube.com")

# driver.close()