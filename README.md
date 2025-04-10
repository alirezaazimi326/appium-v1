
# Appium Android Automation with Frappe Integration 🚀

Automation project for Android app using **Python + Appium**, with backend data management via **Frappe**.

### Features
- ✅ Android App automation via Appium
- ✅ Frappe API integration
- ✅ Drivers management
- ✅ Drivers Log (record automation statuses)
- ✅ Update Driver Status
- ✅ Update or Add License Plates to Driver
- ✅ Update or Add Truck Drivers to Driver
- ✅ Modular architecture for easy maintenance
- ✅ Ready for Dockerization and scaling

---

## 📂 Project Structure

appium_automation/
├── config/
│   └── api_config.py                        # API URLs and credentials
│
├── modules/
│   ├── api/
│   │   ├── driver_api.py                    # Fetch drivers and driver details
│   │   ├── drivers_log_api.py               # Create new Drivers Log records
│   │   ├── update_driver_status_api.py      # Update status field of a driver
│   │   ├── update_driver_plate_api.py       # Add/update License plate table
│   │   └── update_truck_driver_api.py       # Add/update Truck driver table
│   │
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
│   │   ├── step9_final_verification.py
│   │   └── logout.py
│   │
│   ├── errors/
│   │   └── road_bill_active_error.py        # Custom error handling
│   │
│   ├── before_login.py                      # App start & splash screen
│   ├── login.py                             # Login form automation
│   ├── menu.py                              # Menu navigation
│   └── steps_handler.py                     # Runs all step modules in order
│
├── test_drivers_log_api.py                  # Test: create Drivers Log
├── test_update_driver_status_api.py         # Test: update driver status
├── test_update_driver_plate_api.py          # Test: update or add plate
├── test_update_truck_driver_api.py          # Test: update or add truck driver
│
├── main.py                                  # Single-thread Appium runner
├── parallel_runner.py                       # Parallel automation (multi-driver)
├── requirements.txt                         # Python dependencies
├── .gitignore
└── README.md                                # Project documentation


## ⚙️ Setup

1. **Clone repository**

```bash
git clone https://github.com/alirezaazimi326/appium-v1.git
cd appium-v1
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Configure API**

Edit `config/api_config.py`  
Set:
- `FRAPPE_API_BASE_URL`
- `FRAPPE_API_KEY`
- `FRAPPE_API_SECRET`

---

## 🧪 Testing API Modules

### Test Drivers Log API

```bash
python test_drivers_log_api.py
```

### Test Update Driver Status

```bash
python test_update_driver_status_api.py
```

### Test Update or Add Plate Table

```bash
python test_update_driver_plate_api.py
```

### Test Update or Add Truck Driver Table

```bash
python test_update_truck_driver_api.py
```

✅ If everything works, you’ll see success logs in the console and records in your Frappe backend.

---

## 🧩 Roadmap

- [x] Add Drivers Log
- [x] Add Driver Status Update
- [x] Add Plate Table Handler
- [x] Add Truck Driver Table Handler
- [ ] Integrate API calls into main automation flow
- [ ] Add Dockerization (Android Emulator + Appium + Script)
- [ ] Add Logging & Reporting
- [ ] CI/CD for automation pipeline

---

## 👤 Author

- **Alireza Azimi** — [GitHub](https://github.com/alirezaazimi326)

---

## 🤝 Contribution

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📜 License

This project is private for now. All rights reserved.
