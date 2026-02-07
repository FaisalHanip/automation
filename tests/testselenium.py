from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Setup driver
driver = webdriver.Chrome()

# URL dasar
url = "https://faisalhanip.github.io/automation/"

driver.maximize_window()

def buka_login_page():
    driver.get(url)
    time.sleep(2)


def test_login_sukses():
    buka_login_page()
    driver.find_element(By.ID, "username").send_keys("test")
    driver.find_element(By.ID, "password").send_keys("test")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(2)
    assert "dashboard" in driver.current_url or "logout" in driver.page_source
    print("✅ Login sukses - PASS")

def test_login_username_salah():
    buka_login_page()
    driver.find_element(By.ID, "username").send_keys("salah")
    driver.find_element(By.ID, "password").send_keys("test")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(2)
    assert "salah" in driver.page_source.lower() or "gagal" in driver.page_source.lower()
    print("✅ Login gagal (username salah) - PASS")

def test_login_password_salah():
    buka_login_page()
    driver.find_element(By.ID, "username").send_keys("test")
    driver.find_element(By.ID, "password").send_keys("salah")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(2)
    assert "salah" in driver.page_source.lower() or "gagal" in driver.page_source.lower()
    print("✅ Login gagal (password salah) - PASS")

def test_login_field_kosong():
    buka_login_page()
    driver.find_element(By.ID, "username").send_keys("")
    driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(2)
    assert "username" in driver.page_source.lower() or "gagal" in driver.page_source.lower()
    print("✅ Login gagal (field kosong) - PASS")

def test_logout():
    test_login_sukses()  # Login dulu
    logout_btn = driver.find_element(By.TAG_NAME, "button")
    logout_btn.click()
    time.sleep(2)
    assert "login" in driver.page_source.lower()
    print("✅ Logout - PASS")

# Jalankan semua tes
test_login_sukses()
test_login_username_salah()
test_login_password_salah()
test_login_field_kosong()
test_logout()

# Tutup browser
driver.quit()