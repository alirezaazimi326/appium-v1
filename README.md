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
├── modules/
│   ├── login.py
│   ├── menu.py
│   └── steps/
│       ├── step0_verification.py
│       ├── step1_sender_receiver.py
│       ├── step2_car_driver.py
│       ├── step3_cargo.py
│       ├── step4_loading.py
│       ├── step5_unloading.py
│       ├── step6_postal_code.py
│       ├── step7_payment.py
│       ├── step8_summary.py
│       └── final_verification.py
├── main.py
├── requirements.txt
└── README.md
```

## Running the Automation

To run the automation:

```bash
python main.py
```

## Automation Steps

1. System Login
2. Initial Verification
3. Sender and Receiver Information
4. Vehicle and Driver Details
5. Cargo Information
6. Loading Location
7. Unloading Location
8. Postal Code Verification
9. Payment and Document Issuance
10. Summary and Final Submission
11. Final Verification and Return to Home

## Features

- Complete end-to-end automation of transport document creation
- Robust error handling and verification at each step
- Multiple selector strategies (XPath, UiAutomator) for reliable element location
- Automatic captcha reading and input
- Confirmation popup handling
- Final verification and success validation 