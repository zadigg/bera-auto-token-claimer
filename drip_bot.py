import os
import requests
from datetime import datetime

# Define the API endpoint
url = "https://bartiofaucet.berachain.com/api/claim"

# Fetch wallet address from environment variable
wallet_address = os.getenv("WALLET_ADDRESS")

# Ensure wallet address is set
if not wallet_address:
    raise ValueError("WALLET_ADDRESS environment variable is not set")

payload = {"address": wallet_address}

# Send the POST request
try:
    print(f"Sending POST request to {url} with payload: {payload}")

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("Claim successful!")
        print("Response:", response.json())
    else:
        print(f"Error: Received status code {response.status_code}")
        print("Response:", response.text)

except Exception as e:
    print(f"An error occurred: {e}")
