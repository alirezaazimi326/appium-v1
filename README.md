# Transport System Automation

This project is an automation solution for a transport system using Appium and Python.

## Prerequisites

- Python 3.8+
- Appium Server
- Android SDK
- Android Emulator or Physical Device
- pip (Python Package Manager)

## Setup and Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Appium Server Setup:
- Install Appium Server
- Ensure server is running on port 4723

3. Android Setup:
- Install Android SDK
- Set up ANDROID_HOME
- Launch emulator or connect physical device

## Project Structure

```
appium_automation/
├── config/
│   └── api_config.py
├── modules/
│   ├── api/
│   │   └── driver_api.py
│   ├── steps/
│   │   ├── step0_verification.py
│   │   ├── step1_sender_receiver.py
│   │   ├── step2_car_driver.py
│   │   ├── step3_cargo.py
│   │   ├── step4_loading.py
│   │   ├── step5_unloading.py
│   │   ├── step6_postal_code.py
│   │   ├── step7_payment.py
│   │   ├── step8_summary.py
│   │   └── final_verification.py
│   ├── errors/
│   │   └── road_bill_active_error.py
│   ├── before_login.py
│   ├── login.py
│   ├── menu.py
│   └── steps_handler.py
├── main.py
├── parallel_runner.py
├── requirements.txt
└── README.md


```

## Running the Automation

To run the automation:

```bash
python main.py
```

## Automation Steps

1. Login Preparations
2. System Login
3. Initial Verification
4. Sender and Receiver Information
5. Vehicle and Driver Details
6. Cargo Information
7. Loading Location
8. Unloading Location
9. Postal Code Verification
10. Payment and Document Issuance
11. Summary and Final Submission
12. Final Verification and Return to Home

## Features

- Complete end-to-end automation of transport document creation
- API integration for driver information retrieval
- Modular architecture with centralized step handling
- Robust error handling and verification at each step
- Multiple selector strategies (XPath, UiAutomator) for reliable element location
- Automatic captcha reading and input
- Confirmation popup handling
- Final verification and success validation
- Configuration management for API endpoints 