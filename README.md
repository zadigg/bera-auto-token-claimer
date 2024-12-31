
# Automated Drip Script for Bartio Faucet

This repository contains a Python script and a GitHub Actions workflow to automate claiming tokens from the [Bartio Faucet](https://bartio.faucet.berachain.com). The script uses the faucet's API to claim tokens automatically every 8 hours.

---

## Features

- Automatically claims tokens using the faucet API.
- Configured to run every 8 hours using GitHub Actions.
- Logs all responses (success or errors) to a file for easy tracking.

---

## Setup Instructions

### 1. Fork or Clone This Repository
You can fork this repository to your own GitHub account or clone it locally:
```bash
git clone https://github.com/your-username/your-repo-name.git
```

---

### 2. Update the Wallet Address
1. Open the `drip_script.py` file.
2. Replace the placeholder wallet address with your Ethereum wallet address:
   ```python
   payload = {
       "address": "0xYourEthereumWalletAddress"  # Replace with your actual wallet address
   }
   ```
3. Commit your changes:
   ```bash
   git add drip_script.py
   git commit -m "Update wallet address"
   git push origin main
   ```

---

### 3. GitHub Actions Workflow
The repository includes a pre-configured GitHub Actions workflow located at `.github/workflows/run_script.yml`. The workflow:
- Runs the script every 8 hours.
- Automatically installs Python and dependencies.

#### Modifying the Schedule
If you want to change the schedule, update the `cron` expression in `.github/workflows/run_script.yml`:
```yaml
on:
  schedule:
    - cron: "0 */8 * * *"  # Runs every 8 hours
```
Refer to [crontab.guru](https://crontab.guru/) for help with cron expressions.

---

### 4. Run Manually (Optional)
To test the workflow manually:
1. Go to the **Actions** tab in your repository.
2. Select the workflow (e.g., "Run Drip Script").
3. Click **Run workflow**.

---

### 5. View Logs
Logs for each workflow run can be found in the **Actions** tab on GitHub. You can also view detailed responses in the `claim_log.txt` file, which is updated every time the script runs.

---

## Requirements

- Python 3.8 or higher (for local testing).
- Dependencies: Install via:
  ```bash
  pip install requests
  ```
- A GitHub account to use GitHub Actions.

---

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
