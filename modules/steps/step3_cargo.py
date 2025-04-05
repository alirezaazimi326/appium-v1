from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import os

# Add the parent directory to the Python path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from config.settings import CARGO_DETAILS

class Step3CargoModule:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def verify_step_title(self, expected_title="مشخصات کالا"):
        """Verify if we're on the cargo details step"""
        try:
            title_element = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, f'//android.widget.TextView[@text="{expected_title}"]')
            ))
            actual_title = title_element.text
            if actual_title == expected_title:
                print(f"Verified step 3: {actual_title}")
                return True
            else:
                print(f"Step 3 mismatch. Expected: {expected_title}, Found: {actual_title}")
                return False
        except Exception as e:
            print(f"Error verifying step 3 title: {str(e)}")
            return False

    def fill_cargo_name(self, cargo_info=None):
        """Fill in the cargo name and select from dropdown"""
        try:
            if cargo_info is None:
                cargo_info = CARGO_DETAILS

            # Fill cargo name
            name_field = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, '(//android.widget.EditText[@resource-id="RNE__Input__text-input"])[1]')
            ))
            name_field.clear()
            name_field.send_keys(cargo_info['name'])
            print(f"Entered cargo name: {cargo_info['name']}")

            # Wait for dropdown and select the item
            time.sleep(0.5)  # Wait for dropdown to appear
            cargo_item = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, f'//android.view.ViewGroup[@content-desc="{cargo_info["name"]}"]')
            ))
            cargo_item.click()
            print(f"Selected cargo from dropdown: {cargo_info['name']}")

            # Click on packing type dropdown
            packing_dropdown = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc=""]/android.widget.TextView')
            ))
            packing_dropdown.click()
            print("Clicked on packing type dropdown")

            # Select packing type
            time.sleep(0.5)  # Wait for dropdown to appear
            packing_type = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, f'//android.view.ViewGroup[@content-desc="{cargo_info["packing_type"]}"]')
            ))
            packing_type.click()
            print(f"Selected packing type: {cargo_info['packing_type']}")

            # Fill weight
            weight_field = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, '(//android.widget.EditText[@resource-id="RNE__Input__text-input"])[2]')
            ))
            weight_field.clear()
            weight_field.send_keys(cargo_info['weight'])
            print(f"Entered weight: {cargo_info['weight']}")

            # Fill packages count
            packages_field = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, '(//android.widget.EditText[@resource-id="RNE__Input__text-input"])[3]')
            ))
            packages_field.clear()
            packages_field.send_keys(cargo_info['packages_count'])
            print(f"Entered packages count: {cargo_info['packages_count']}")

            # Click add cargo button
            add_button = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="iconIcon" and @text=""]')
            ))
            add_button.click()
            print("Clicked add cargo button")
            
            return True
        except Exception as e:
            print(f"Error filling cargo details: {str(e)}")
            return False

    def complete_cargo_details(self, cargo_info=None):
        """Fill additional cargo details after adding cargo"""
        try:
            if cargo_info is None:
                cargo_info = CARGO_DETAILS

            # Fill cargo value
            value_field = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="RNE__Input__text-input" and @text="0"]')
            ))
            value_field.clear()
            value_field.send_keys(cargo_info['value'])
            print(f"Entered cargo value: {cargo_info['value']}")

            # Click on checkbox
            checkbox = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="checkboxTitle"]')
            ))
            checkbox.click()
            print("Clicked on checkbox")

            # Click continue button
            continue_button = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="ادامه"]')
            ))
            continue_button.click()
            print("Clicked continue button")
            
            return True
        except Exception as e:
            print(f"Error completing cargo details: {str(e)}")
            return False

    def fill_and_continue(self, cargo_info=None):
        """Complete cargo details and continue to next step"""
        try:
            if self.verify_step_title():
                if not self.fill_cargo_name(cargo_info):
                    return False
                time.sleep(1)  # Wait for any animations
                if not self.complete_cargo_details(cargo_info):
                    return False
                return True
            return False
        except Exception as e:
            print(f"Step 3 cargo details failed with error: {str(e)}")
            return False 