import requests
from config import api_config

session = requests.Session()
session.headers.update({
    "Authorization": f"token {api_config.FRAPPE_API_KEY}:{api_config.FRAPPE_API_SECRET}"
})

def create_driver_log(driver_name: str, status: str, log_type: str = "submit"):
    """
    Create a new Drivers Log record in Frappe.

    Args:
        driver_name (str): The name of the driver (linked to the Drivers doctype).
        status (str): Status message like 'Wrong Password', 'Road Bill Active', 'Success', etc.
    """
    payload = {
        "driver": driver_name,
        "status": status,
        "log_type": log_type
    }

    try:
        response = session.post(api_config.DRIVERS_LOG_API, json=payload)
        response.raise_for_status()
        data = response.json()
        print(f"[Drivers Log] New log created for driver '{driver_name}' with status '{status}'.")
        return data
    except requests.RequestException as e:
        print(f"[Drivers Log] Failed to create log for driver '{driver_name}'. Error: {e}")
        return None
