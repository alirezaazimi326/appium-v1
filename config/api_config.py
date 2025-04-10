FRAPPE_API_BASE_URL = "http://45.139.10.113:8002"

# Endpoints
FRAPPE_API_DRIVERS_ENDPOINT = "/api/resource/Drivers"
FRAPPE_API_LOG_DRIVERS_ENDPOINT = "/api/resource/Drivers Log"
FRAPPE_API_EMULATOR_ENDPOINT = "/api/resource/Emulator"

# Authentication
FRAPPE_API_KEY = "526c1187d506852"
FRAPPE_API_SECRET = "941ef853fbc951c"

# Constructed full URLs
DRIVERS_LIST_URL = f"{FRAPPE_API_BASE_URL}{FRAPPE_API_DRIVERS_ENDPOINT}"
DRIVERS_LOG_API = f"{FRAPPE_API_BASE_URL}{FRAPPE_API_LOG_DRIVERS_ENDPOINT}"
EMULATOR_LIST_URL = f"{FRAPPE_API_BASE_URL}{FRAPPE_API_EMULATOR_ENDPOINT}"

def get_driver_detail_url(driver_id: str) -> str:
    """Construct URL for specific driver details"""
    return f"{FRAPPE_API_BASE_URL}{FRAPPE_API_DRIVERS_ENDPOINT}/{driver_id}"
