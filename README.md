# اتوماسیون سامانه حمل و نقل

این پروژه یک اتوماسیون برای سامانه حمل و نقل با استفاده از Appium و Python است.

## پیش‌نیازها

- Python 3.8+
- Appium Server
- Android SDK
- Android Emulator یا دستگاه فیزیکی
- pip (Python Package Manager)

## نصب و راه‌اندازی

1. نصب وابستگی‌ها:
```bash
pip install -r requirements.txt
```

2. تنظیم Appium Server:
- نصب Appium Server
- اطمینان از اجرای سرور در پورت 4723

3. تنظیم Android:
- نصب Android SDK
- تنظیم ANDROID_HOME
- راه‌اندازی شبیه‌ساز یا اتصال دستگاه فیزیکی

## ساختار پروژه

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

## اجرا

برای اجرای اتوماسیون:

```bash
python main.py
```

## مراحل اتوماسیون

1. ورود به سیستم
2. تایید اولیه
3. اطلاعات فرستنده و گیرنده
4. اطلاعات ماشین و راننده
5. اطلاعات محموله
6. محل بارگیری
7. محل تخلیه
8. تایید کد پستی
9. پرداخت و صدور سند
10. خلاصه و ثبت نهایی
11. تایید نهایی و بازگشت به صفحه اصلی 