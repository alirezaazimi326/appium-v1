from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os

# Add the parent directory to the Python path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.api.driver_api import DriverAPI

class LoginModule:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.api = DriverAPI()
        self.driver_details = None

    def get_credentials(self, phone_number):
        """Get user credentials and details from API"""
        try:
            self.driver_details = self.api.get_driver_by_phone(phone_number)
            if self.driver_details:
                return {
                    'phone_number': self.driver_details['user_name'],
                    'password': self.driver_details['password']
                }
            return None
        except Exception as e:
            print(f"Error getting credentials from API: {str(e)}")
            return None

    def enter_phone_number(self, phone_number):
        """Enter phone number in the phone field"""
        try:
            # Remove '09' prefix if exists
            if phone_number.startswith('09'):
                phone_number = phone_number[2:]
            
            phone_field = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="RNE__Input__text-input" and @text="09"]')
            ))
            phone_field.send_keys(phone_number)
            print(f"Entered phone number: 09{phone_number}")
            return True
        except Exception as e:
            print(f"Error entering phone number: {str(e)}")
            return False

    def enter_password(self, password):
        """Enter password in the password field"""
        try:
            password_field = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, '(//android.widget.EditText[@resource-id="RNE__Input__text-input"])[2]')
            ))
            password_field.clear()
            password_field.send_keys(password)
            print("Entered password")
            return True
        except Exception as e:
            print(f"Error entering password: {str(e)}")
            return False

    def click_login_button(self):
        """Click on the login button"""
        try:
            # Try first with content-desc (most reliable)
            login_button = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.ACCESSIBILITY_ID, "ورود")
            ))
            login_button.click()
            print("Clicked login button using accessibility ID")
            return True
        except Exception as e:
            print("Could not find login button by accessibility ID, trying alternative method...")
            try:
                # Fallback to class and bounds if content-desc fails
                login_button = self.wait.until(EC.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.view.ViewGroup[@bounds="[96,1463][984,1541]"]')
                ))
                login_button.click()
                print("Clicked login button using bounds")
                return True
            except Exception as e:
                print(f"Error clicking login button: {str(e)}")
                return False

    def perform_login(self, phone_number):
        """Perform complete login process using API credentials"""
        try:
            credentials = self.get_credentials(phone_number)
            if not credentials:
                print("Could not find user credentials in API")
                return None

            if not self.enter_phone_number(credentials['phone_number']):
                return None
            if not self.enter_password(credentials['password']):
                return None
            if not self.click_login_button():
                return None
                
            return self.driver_details
        except Exception as e:
            print(f"Login failed with error: {str(e)}")
            return None 