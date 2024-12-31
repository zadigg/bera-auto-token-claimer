import requests
from datetime import datetime


url = "https://bartiofaucet.berachain.com/api/claim"
payload = {
    "address": "0x3262902343C16C54Be3C33e6F7b9FDE5C5FD39eD"  # Replace with your Ethereum wallet address
}


log_file = "claim_log.txt"


def log_to_file(message):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open(log_file, "a") as file:
        file.write(f"{timestamp} {message}\n")

try:
    print(f"Sending POST request to {url} with payload: {payload}")

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        message = "Claim successful!"
        print(message)
        print("Response:", response.json())
        log_to_file(message)
        log_to_file(f"Response: {response.json()}")
    else:
        message = f"Error: Received status code {response.status_code}"
        print(message)
        print("Response:", response.text)
        log_to_file(f"{response.status_code}: {response.text}")

except Exception as e:
    error_message = f"An error occurred: {e}"
    print(error_message)
    log_to_file(error_message)
