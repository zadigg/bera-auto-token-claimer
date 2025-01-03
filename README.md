
# Automated Drip Script for Bartio Faucet

This repository contains a Python script and a GitHub Actions workflow to automate claiming tokens from the [Bartio Faucet](https://bartio.faucet.berachain.com). The script uses the faucet's API to claim tokens automatically every 8 hours.

---

## Features

- Automatically claims tokens using the faucet API.
- Fetches wallet address securely from an environment variable.
- Configured to run every 8 hours using GitHub Actions.

---

## Setup Instructions

### **Important**
To successfully run this script, you must complete **Step 1** (Fork the repository) and **Step 2** (Set up the wallet address).

---

### 1. Fork or Clone This Repository
Fork this repository to your own

---

### 2. Set Up the Wallet Address
The script fetches the wallet address from an environment variable called `WALLET_ADDRESS`. Follow these steps to set it up securely:

1. Navigate to your GitHub repository.
2. Go to **Settings** > **Secrets and variables** > **Actions** > **New repository secret**.
3. Add a new secret:
   - **Name**: `WALLET_ADDRESS`
   - **Value**: `0xYourEthereumWalletAddress` (replace with your actual wallet address).
4. Save the secret.

---

### 3. GitHub Actions Workflow  
The repository includes a pre-configured GitHub Actions workflow located at `.github/workflows/run_script.yml`. The workflow:
- Runs the script every 8 hours.
- Passes the wallet address securely to the script using GitHub Secrets.
- Automatically installs Python and dependencies.

#### Modifying the Schedule
If you want to change the schedule, update the `cron` expression in `.github/workflows/run_script.yml`:
```yaml
on:
  schedule:
    - cron: "0 */8 * * *"  # Runs every 8 hours
```
Refer to [crontab.guru](https://crontab.guru/) for help with cron expressions.

Evry 8 hours you see new workflow in the action tab 

![image](https://github.com/user-attachments/assets/ed1642c4-cc93-4377-984e-f2132bf1446f)


---

### 4. Run Manually (Optional)
To test the workflow manually:
1. Go to the **Actions** tab in your repository.
2. Select the workflow (e.g., "Run Drip Script").
3. Click **Run workflow**.

---

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
