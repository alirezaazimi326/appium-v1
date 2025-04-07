from appium import webdriver
import os
from selenium.webdriver.support.ui import WebDriverWait
from modules.before_login import BeforeLoginModule
from modules.steps_handler import StepsHandler
from modules.api.driver_api import DriverAPI

# Appium Desired Capabilities Configuration
desired_caps = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'avd': 'Pixel_7_Edited_API_34_Num_2',  # <-- AVD name from your emulator config
    'app': os.path.join(os.getcwd(), 'com.transport.apk'),
    'noReset': True,
    'newCommandTimeout': 3600,
    'platformVersion': '14.0',  # Make sure this matches your emulator version
    'autoGrantPermissions': True
}

def is_app_running(driver, package_name):
    """Check if the app is already running on the device"""
    current_package = driver.current_package
    return current_package == package_name

try:
    # Initialize API and get list of drivers
    api = DriverAPI()
    drivers_list = api.get_drivers_list()
    
    if not drivers_list:
        raise Exception("No drivers found in API")
    
    print(f"Found {len(drivers_list)} drivers to process")
    
    # Initialize Appium driver with local server
    driver = webdriver.Remote('http://127.0.0.1:4723', desired_caps)

    # Check if the app is already running (skip opening if it is)
    if is_app_running(driver, 'com.transport'):
        print("App is already open, skipping launch.")
    else:
        print("Launching app...")
        driver.launch_app()  # Only launch if app is not running
        
    wait = WebDriverWait(driver, 20)


    
    # Handle initial continue button
    before_login = BeforeLoginModule(driver)
    if not before_login.click_continue():
        raise Exception("Failed to click initial continue button")
    
    # Initialize steps handler
    steps_handler = StepsHandler(driver)
    
    # Process each driver
    for driver_id in drivers_list:
        print(f"\nProcessing driver {driver_id}")
        driver_details = api.get_driver_details(driver_id)
        
        if driver_details:
            if steps_handler.process_driver(driver_details):
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