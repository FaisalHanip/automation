from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_example_domain():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get("https://faisalhanip.github.io/automation/")

    assert "Login" in driver.title

    driver.quit()