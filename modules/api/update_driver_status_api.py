import requests
from config import api_config

# Initialize session with authentication
session = requests.Session()
session.headers.update({
    "Authorization": f"token {api_config.FRAPPE_API_KEY}:{api_config.FRAPPE_API_SECRET}"
})

def update_driver_status(driver_id: str, status: str):
    """
    Update the status field of an existing Driver record.

    Args:
        driver_id (str): The ID of the driver (e.g., 'DRV00002').
        status (str): The new status to set (e.g., 'Normal', 'Blocked', etc.)

    Returns:
        dict: API response, or None if failed.
    """
    payload = {
        "status": status
    }

    url = api_config.get_driver_detail_url(driver_id)

    try:
        response = session.put(url, json=payload)
        response.raise_for_status()
        print(f"[Drivers API] Successfully updated driver '{driver_id}' to status '{status}'.")
        return response.json()
    except requests.RequestException as e:
        print(f"[Drivers API] Failed to update driver '{driver_id}'. Error: {e}")
        return None
