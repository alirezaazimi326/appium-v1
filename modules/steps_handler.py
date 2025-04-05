from .login import LoginModule
from .menu import MenuModule
from .steps.step0_verification import Step0VerificationModule
from .steps.step1_sender_receiver import Step1SenderReceiverModule
from .steps.step2_car_driver import Step2CarDriverModule
from .steps.step3_cargo import Step3CargoModule
from .steps.step4_loading import Step4LoadingModule
from .steps.step5_unloading import Step5UnloadingModule
from .steps.step6_postal_code import Step6PostalCodeModule
from .steps.step7_payment import Step7PaymentModule
from .steps.step8_summary import Step8SummaryModule
from .steps.final_verification import FinalVerificationModule
from .steps.logout import LogoutModule
from .steps.sms_check import SmsCheckModule

class StepsHandler:
    def __init__(self, driver):
        self.driver = driver

    def process_driver(self, driver_details):
        """Process all steps for a single driver"""
        try:
            # Login
            login = LoginModule(self.driver)
            if not login.perform_login(driver_details['user_name']):
                print("Login failed!")
                return False

            print(f"Login successful for driver {driver_details['user_name']}!")
            
            # Menu
            menu = MenuModule(self.driver)
            if not menu.click_and_wait():
                print("Menu interaction failed!")
                return False

            print("Menu interaction successful!")
            
            # Step 0: Initial Verification
            step0 = Step0VerificationModule(self.driver)
            if not step0.verify_and_continue():
                print("Step 0 failed!")
                return False

            print("Step 0 completed successfully!")
            print(" /n ****************")
            
            # Step 1: Sender and Receiver Details
            step1 = Step1SenderReceiverModule(self.driver)
            step1.set_driver_details(driver_details)
            if not step1.fill_and_continue():
                print("Step 1 failed!")
                return False

            print("Step 1 completed successfully!")
            print(" /n ****************")

            # Step 2: Car and Driver Details
            step2 = Step2CarDriverModule(self.driver)
            if not step2.select_car_and_continue():
                print("Step 2 failed!")
                return False

            print("Step 2 completed successfully!")
            print(" /n ****************")

            # Step 3: Cargo Details
            step3 = Step3CargoModule(self.driver)
            step3.set_driver_details(driver_details)
            if not step3.fill_and_continue():
                print("Step 3 failed!")
                return False

            print("Step 3 completed successfully!")
            print(" /n ****************")

            # Step 4: Loading Location
            step4 = Step4LoadingModule(self.driver)
            if not step4.select_loading_location():
                print("Step 4 failed!")
                return False

            print("Step 4 completed successfully!")
            print("/n ****************")

            # Step 5: Unloading Location
            step5 = Step5UnloadingModule(self.driver)
            if not step5.select_unloading_location():
                print("Step 5 failed!")
                return False

            print("Step 5 completed successfully!")
            print("/n ****************")

            # Step 6: Postal Code Verification
            step6 = Step6PostalCodeModule(self.driver)
            if not step6.verify_and_continue():
                print("Step 6 failed!")
                return False

            print("Step 6 completed successfully!")
            print("/n ****************")

            # Step 7: Payment and Document
            step7 = Step7PaymentModule(self.driver)
            if not step7.verify_and_continue():
                print("Step 7 failed!")
                return False

            print("Step 7 completed successfully!")
            print("/n ****************")

            # Step 8: Summary and Submit
            step8 = Step8SummaryModule(self.driver)
            if not step8.verify_and_submit():
                print("Step 8 failed!")
                return False

            print("Step 8 completed successfully!")
            print("/n ****************")
            
            # Check for SMS verification
            sms_check = SmsCheckModule(self.driver)
            sms_check.check_sms_prompt()

            # Final Verification
            final_verify = FinalVerificationModule(self.driver)
            if not final_verify.verify_success():
                print("Final verification failed!")
                return False

            print("Final verification passed - Found success message")
            print("/n ****************")
            
            # Return to home page
            if not final_verify.back_to_home():
                print("Failed to return to home page")
                return False

            print("Successfully returned to home page")
            
            # Logout
            logout = LogoutModule(self.driver)
            if not logout.perform_logout():
                print("Failed to logout")
                return False

            print("Successfully logged out")
            return True

        except Exception as e:
            print(f"Error processing driver {driver_details['user_name']}: {str(e)}")
            return False 