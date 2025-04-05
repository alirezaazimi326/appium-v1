from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from modules.login import LoginModule
from modules.menu import MenuModule
from modules.steps.step0_verification import Step0VerificationModule
from modules.steps.step1_sender_receiver import Step1SenderReceiverModule
from modules.steps.step2_car_driver import Step2CarDriverModule
from modules.steps.step3_cargo import Step3CargoModule
from modules.steps.step4_loading import Step4LoadingModule
from modules.steps.step5_unloading import Step5UnloadingModule
from modules.steps.step6_postal_code import Step6PostalCodeModule
from modules.steps.step7_payment import Step7PaymentModule
from modules.steps.step8_summary import Step8SummaryModule
from modules.steps.final_verification import FinalVerificationModule
from modules.steps.logout import LogoutModule
from modules.steps.sms_check import SmsCheckModule
from modules.api.driver_api import DriverAPI

def process_driver(driver, driver_details):
    """Process a single driver's workflow"""
    try:
        # Initialize login module and perform login
        login = LoginModule(driver)
        login_success = login.perform_login(driver_details['user_name'])
        
        if login_success:
            print(f"Login successful for driver {driver_details['user_name']}!")
            
            # Initialize menu module and open menu
            menu = MenuModule(driver)
            menu_success = menu.click_and_wait()
            
            if menu_success:
                print("Menu interaction successful!")
                
                # Step 0: Initial Verification
                step0 = Step0VerificationModule(driver)
                if step0.verify_and_continue():
                    print("Step 0 completed successfully!")
                    print(" /n ****************")
                    
                    # Step 1: Sender and Receiver Details
                    step1 = Step1SenderReceiverModule(driver)
                    step1.set_driver_details(driver_details)  # Set API data
                    if step1.fill_and_continue():
                        print("Step 1 completed successfully!")
                        print(" /n ****************")

                        # Step 2: Car and Driver Details
                        step2 = Step2CarDriverModule(driver)
                        if step2.select_car_and_continue():
                            print("Step 2 completed successfully!")
                            print(" /n ****************")

                            # Step 3: Cargo Details
                            step3 = Step3CargoModule(driver)
                            step3.set_driver_details(driver_details)  # Set API data
                            if step3.fill_and_continue():
                                print("Step 3 completed successfully!")
                                print(" /n ****************")

                                # Step 4: Loading Location
                                step4 = Step4LoadingModule(driver)
                                if step4.select_loading_location():
                                    print("Step 4 completed successfully!")
                                    print("/n ****************")

                                    # Step 5: Unloading Location
                                    step5 = Step5UnloadingModule(driver)
                                    if step5.select_unloading_location():
                                        print("Step 5 completed successfully!")
                                        print("/n ****************")

                                        # Step 6: Postal Code Verification
                                        step6 = Step6PostalCodeModule(driver)
                                        if step6.verify_and_continue():
                                            print("Step 6 completed successfully!")
                                            print("/n ****************")

                                            # Step 7: Payment and Document
                                            step7 = Step7PaymentModule(driver)
                                            if step7.verify_and_continue():
                                                print("Step 7 completed successfully!")
                                                print("/n ****************")

                                                # Step 8: Summary and Submit
                                                step8 = Step8SummaryModule(driver)
                                                if step8.verify_and_submit():
                                                    print("Step 8 completed successfully!")
                                                    print("/n ****************")
                                                    
                                                    # Check for SMS verification
                                                    sms_check = SmsCheckModule(driver)
                                                    sms_check.check_sms_prompt()  # This will exit if SMS prompt is found

                                                    # Final Verification
                                                    final_verify = FinalVerificationModule(driver)
                                                    if final_verify.verify_success():
                                                        print("All steps completed successfully!")
                                                        print("Final verification passed - Found success message")
                                                        print("/n ****************")
                                                        
                                                        # Return to home page
                                                        if final_verify.back_to_home():
                                                            print("Successfully returned to home page")
                                                            
                                                            # Perform logout
                                                            logout = LogoutModule(driver)
                                                            if logout.perform_logout():
                                                                print("Successfully logged out")
                                                                return True
                                                            else:
                                                                print("Failed to logout")
                                                                return False
                                                        else:
                                                            print("Failed to return to home page")
                                                    else:
                                                        print("Final verification failed!")
                                                else:
                                                    print("Step 8 failed!")
                                            else:
                                                print("Step 7 failed!")
                                        else:
                                            print("Step 6 failed!")
                                    else:
                                        print("Step 5 failed!")
                                else:
                                    print("Step 4 failed!")
                            else:
                                print("Step 3 failed!")
                        else:
                            print("Step 2 failed!")
                    else:
                        print("Step 1 failed!")
                else:
                    print("Step 0 failed!")
            else:
                print("Menu interaction failed!")
        else:
            print("Login failed!")
        
        return False
    except Exception as e:
        print(f"Error processing driver {driver_details['user_name']}: {str(e)}")
        return False

# Appium Desired Capabilities Configuration
desired_caps = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'deviceName': 'emulator-5554',
    'app': os.path.join(os.getcwd(), 'com.transport.apk'),
    'noReset': True,
    'newCommandTimeout': 3600,
    'platformVersion': '14.0',  # Make sure this matches your emulator version
    'autoGrantPermissions': True
}

try:
    # Initialize API and get list of drivers
    api = DriverAPI()
    drivers_list = api.get_drivers_list()
    
    if not drivers_list:
        raise Exception("No drivers found in API")
    
    print(f"Found {len(drivers_list)} drivers to process")
    
    # Initialize Appium driver with local server
    driver = webdriver.Remote('http://127.0.0.1:4723', desired_caps)
    wait = WebDriverWait(driver, 20)
    
    # Wait and click on Continue button (ادامه)
    continue_button = wait.until(EC.presence_of_element_located(
        (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="ادامه"]')
    ))
    print("Found Continue button, clicking it...")
    continue_button.click()
    time.sleep(1)
    
    # Process each driver
    for driver_id in drivers_list:
        print(f"\nProcessing driver {driver_id}")
        driver_details = api.get_driver_details(driver_id)
        
        if driver_details:
            if process_driver(driver, driver_details):
                print(f"Successfully processed driver {driver_id}")
            else:
                print(f"Failed to process driver {driver_id}")
        else:
            print(f"Could not get details for driver {driver_id}")

except Exception as e:
    print(f"Error occurred: {str(e)}")

finally:
    # Always close the driver to end the session
    driver.quit() 