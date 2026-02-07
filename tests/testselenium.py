from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_open_homepage():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://github.com/FaisalHanip/automation")
    assert "Login Sederhana" in driver.title
    driver.quit()
