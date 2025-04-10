import requests
import subprocess
import time
from config.api_config import FRAPPE_API_BASE_URL, FRAPPE_API_KEY, FRAPPE_API_SECRET

# Function to fetch the list of emulators from the Frappe API
def fetch_emulators():
    url = f"{FRAPPE_API_BASE_URL}/api/resource/Emulator"
    headers = {
        "Authorization": f"token {FRAPPE_API_KEY}:{FRAPPE_API_SECRET}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        emulators = response.json().get('data', [])
        print(f"Fetched Emulators: {emulators}")
        return emulators
    else:
        print("Error fetching emulators.")
        return []

# Function to fetch the details of a specific emulator from Frappe
def fetch_emulator_details(emulator_name):
    url = f"{FRAPPE_API_BASE_URL}/api/resource/Emulator/{emulator_name}"
    headers = {
        "Authorization": f"token {FRAPPE_API_KEY}:{FRAPPE_API_SECRET}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        emulator_details = response.json().get('data', {})
        print(f"Fetched details for {emulator_name}: {emulator_details}")
        return emulator_details
    else:
        print(f"Error fetching details for emulator {emulator_name}.")
        return {}

# Function to start the emulator with the given AVD name
def start_emulator(avd_name):
    print(f"Starting emulator {avd_name}...")
    try:
        subprocess.Popen(['emulator', '-avd', avd_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Emulator {avd_name} started.")
    except Exception as e:
        print(f"Error starting emulator {avd_name}: {e}")
        return False
    return True

# Function to check if the emulator is booted by checking adb devices
def is_emulator_booted():
    print("Waiting for the emulator to boot...")
    timeout = 300  # Timeout in seconds (5 minutes)
    start_time = time.time()

    while True:
        try:
            # Check connected devices using adb
            result = subprocess.check_output(['adb', 'devices'], stderr=subprocess.STDOUT)
            devices = result.decode('utf-8').splitlines()

            # If the emulator is booted, it should appear in the adb devices list
            for device in devices:
                if device.endswith('device'):
                    print(f"Emulator is booted and connected: {device}")
                    return True
        except subprocess.CalledProcessError as e:
            print(f"Error checking adb devices: {e.output.decode()}")

        # Check if timeout has exceeded
        if time.time() - start_time > timeout:
            print("Timeout reached. Emulator did not boot.")
            break

        # Wait for 5 seconds before checking again
        time.sleep(5)

    return False

# Function to update the status of the emulator to "Online" in Frappe
def update_emulator_status_to_online(emulator_name):
    url = f"{FRAPPE_API_BASE_URL}/api/resource/Emulator/{emulator_name}"
    headers = {
        "Authorization": f"token {FRAPPE_API_KEY}:{FRAPPE_API_SECRET}",
        "Content-Type": "application/json"
    }
    data = {
        "status": "Online"
    }
    response = requests.put(url, headers=headers, json=data)
    
    if response.status_code == 200:
        print(f"Emulator {emulator_name} status updated to 'Online'.")
    else:
        print(f"Error updating status for emulator {emulator_name}: {response.text}")

# Main function to manage emulators (only starts the emulators)
def manage_emulators():
    emulators = fetch_emulators()
    
    if not emulators:
        print("No emulators found.")
        return

    for emulator in emulators:
        emulator_name = emulator.get('name')  # Get the emulator name
        if emulator_name:
            # Fetch the emulator details
            emulator_details = fetch_emulator_details(emulator_name)

            # Get the device name and start the AVD emulator
            device_name = emulator_details.get('device_name')

            if device_name:
                print(f"Starting AVD: {device_name}")
                if start_emulator(device_name):
                    # Check if the emulator is booted
                    if is_emulator_booted():
                        print(f"Emulator {device_name} booted successfully.")
                        # Update the status of the emulator to 'Online'
                        update_emulator_status_to_online(emulator_name)
                    else:
                        print(f"Emulator {device_name} failed to boot.")
            else:
                print(f"Device name not found for emulator {emulator_name}.")
        else:
            print(f"Emulator {emulator_name} does not have a valid name.")

if __name__ == "__main__":
    manage_emulators()
