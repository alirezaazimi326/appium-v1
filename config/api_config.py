FRAPPE_API_BASE_URL = "http://45.139.10.113:8001"
FRAPPE_API_DRIVERS_ENDPOINT = "/api/resource/Drivers"

# Construct full URLs
DRIVERS_LIST_URL = f"{FRAPPE_API_BASE_URL}{FRAPPE_API_DRIVERS_ENDPOINT}"

def get_driver_detail_url(driver_id: str) -> str:
    """Construct URL for specific driver details"""
    return f"{FRAPPE_API_BASE_URL}{FRAPPE_API_DRIVERS_ENDPOINT}/{driver_id}" 