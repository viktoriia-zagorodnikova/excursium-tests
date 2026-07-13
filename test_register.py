import os
import time
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

TEST_EMAIL = os.environ.get("TEST_EMAIL")

BASE_URL = "https://excursium.com/Client/Login"


class TestRegister:
    def test_registration_with_existing_email(self, driver):
        """EX-009: Registration with an already existing email"""
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)
        reg_tab = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Регистрация')]")))
        reg_tab.click()
        time.sleep(2)
        email = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'view active')]//input[@placeholder='Ваша электронная почта']")))
        email.send_keys(TEST_EMAIL)
        password = driver.find_element(
            By.XPATH, "//div[contains(@class,'view active')]//input[@placeholder='Минимум 6 символов']")
        password.send_keys("test_password123")
        checkbox = driver.find_element(
            By.XPATH, "//input[@type='checkbox']")
        driver.execute_script("arguments[0].click();", checkbox)
        driver.find_element(By.ID, "registraion-btn").click()
        time.sleep(2)
        # Check that the error element is present in the DOM
        errors = driver.find_elements(
            By.XPATH, "//*[contains(text(),'В системе уже есть пользователь с такой почтой')]")
        assert len(errors) > 0

    def test_password_is_hidden(self, driver):
        """EX-013: Password field is masked during registration"""
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)
        reg_tab = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Регистрация')]")))
        reg_tab.click()
        password = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Минимум 6 символов']")))
        assert password.get_attribute("type") == "password"
