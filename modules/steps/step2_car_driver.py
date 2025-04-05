from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import os

class Step2CarDriverModule:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def verify_step_title(self):
        """Verify if we're on step 2 by checking the title"""
        try:
            title_element = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="مشخصات راننده و خودرو"]')
            ))
            if title_element.is_displayed():
                print("Step 2 verification successful - Found driver and car details title")
                return True
            return False
        except Exception as e:
            print(f"Step 2 verification failed: {str(e)}")
            return False

    def click_plate_selector(self):
        """Click on the license plate selector"""
        try:
            # First attempt with text
            try:
                plate_selector = self.wait.until(EC.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.widget.TextView[@text="انتخاب پلاک"]')
                ))
                plate_selector.click()
                print("Selected plate selector using text")
                return True
            except Exception:
                print("Could not find plate selector by text, trying resource-id...")
                
                # Second attempt with resource-id
                try:
                    plate_selector = self.wait.until(EC.presence_of_element_located(
                        (AppiumBy.XPATH, '(//android.widget.TextView[@resource-id="iconIcon"])[4]')
                    ))
                    plate_selector.click()
                    print("Selected plate selector using resource-id")
                    return True
                except Exception:
                    print("Could not find plate selector by resource-id, trying content-desc...")
                    
                    # Third attempt with content-desc
                    plate_selector = self.wait.until(EC.presence_of_element_located(
                        (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="انتخاب پلاک, "]')
                    ))
                    plate_selector.click()
                    print("Selected plate selector using content-desc")
                    return True
        except Exception as e:
            print(f"Failed to click plate selector: {str(e)}")
            return False

    def verify_and_select_plate(self):
        """Verify license plate list is open and select a plate"""
        try:
            # Verify list is open
            list_title = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="فهرست خودرو ها"]')
            ))
            if list_title.is_displayed():
                print("License plate list is open")
                
                # First attempt with instance
                try:
                    plate = self.wait.until(EC.presence_of_element_located(
                        (AppiumBy.XPATH, '(//android.view.ViewGroup[@clickable="true"])[3]')
                    ))
                    plate.click()
                    print("Selected license plate using instance")
                    return True
                except Exception:
                    print("Could not select plate with instance, trying second method...")
                    
                    # Second attempt with full path
                    try:
                        plate = self.wait.until(EC.presence_of_element_located(
                            (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]')
                        ))
                        plate.click()
                        print("Selected license plate using full path")
                        return True
                    except Exception:
                        print("Could not select plate with full path, trying UiAutomator...")
                        
                        # Third attempt with UiAutomator
                        plate = self.driver.find_element(
                            AppiumBy.ANDROID_UIAUTOMATOR,
                            'new UiSelector().className("android.view.ViewGroup").clickable(true).instance(2)'
                        )
                        plate.click()
                        print("Selected license plate using UiAutomator")
                        return True
            return False
        except Exception as e:
            print(f"Failed to verify or select license plate: {str(e)}")
            return False

    def click_driver_selector(self):
        """Click on the driver selector dropdown"""
        try:
            # First attempt with content-desc
            try:
                driver_selector = self.wait.until(EC.presence_of_element_located(
                    (AppiumBy.XPATH, '(//android.widget.TextView[@resource-id="iconIcon"])[5]')
                ))
                driver_selector.click()
                print("Clicked driver selector using resource-id")
                return True
            except Exception:
                print(f"Failed to click driver selector: {str(e)}")                
                # Second attempt with resource-id
                driver_selector = self.wait.until(EC.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc=""]/android.widget.TextView')
                ))
                driver_selector.click()
                print("Clicked driver selector using content-desc")             
                return True
        except Exception as e:
                print("Could not find driver selector by content-desc, trying resource-id...")
                return False

    def click_continue(self):
        """Click on the continue button"""
        try:
            # First attempt with content-desc
            try:
                continue_button = self.wait.until(EC.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="ادامه"]')
                ))
                continue_button.click()
                print("Clicked continue button using content-desc")
                return True
            except Exception:
                print("Could not find continue button by content-desc, trying text...")
                
                # Second attempt with text
                continue_button = self.wait.until(EC.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.widget.TextView[@text="ادامه"]')
                ))
                continue_button.click()
                print("Clicked continue button using text")
                return True
        except Exception as e:
            print(f"Failed to click continue button: {str(e)}")
            return False

    def verify_and_select_driver(self):
        """Verify driver list is open and select a driver"""
        try:
            # Verify driver list is open
            list_title = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="فهرست راننده ها"]')
            ))
            if list_title.is_displayed():
                print("Driver list is open")
                
                # First attempt with XPath
                try:
                    driver = self.wait.until(EC.presence_of_element_located(
                        (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]')
                    ))
                    driver.click()
                    print("Selected driver using XPath")
                    return True
                except Exception:
                    print("Could not select driver with XPath, trying UiAutomator...")
                    
                    # Second attempt with UiAutomator
                    driver = self.driver.find_element(
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.ViewGroup").instance(6)'
                    )
                    driver.click()
                    print("Selected driver using UiAutomator")
                    return True
            return False
        except Exception as e:
            print(f"Failed to verify or select driver: {str(e)}")
            return False

    def select_car_and_continue(self):
        """Complete car selection process"""
        try:
            if self.verify_step_title():
                time.sleep(1)  # Wait for animations
                if not self.click_plate_selector():
                    return False
                time.sleep(1)  # Wait for list to load
                if not self.verify_and_select_plate():
                    return False
                time.sleep(1)  # Wait for animations
                if not self.click_driver_selector():
                    return False
                time.sleep(1)  # Wait for list to load
                if not self.verify_and_select_driver():
                    return False
                time.sleep(1)  # Wait for animations
                if not self.click_continue():
                    return False
                return True
            return False
        except Exception as e:
            print(f"Step 2 car selection failed: {str(e)}")
            return False