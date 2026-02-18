# OpenClaw Oura Skill 💍

Connect your Oura Ring to OpenClaw to fetch sleep, activity, and readiness data directly from the CLI.

## Setup

1.  **Get your Personal Access Token (PAT):**
    - Go to [Oura Cloud › Personal Access Tokens](https://cloud.ouraring.com/personal-access-tokens)
    - Click "Create New Personal Access Token"
    - Give it a name (e.g., `OpenClaw`)
    - Copy the token string.

2.  **Configure Environment:**
    Add the token to your shell environment or OpenClaw config:
    ```bash
    export OURA_ACCESS_TOKEN="your_token_here"
    ```

3.  **Install Skill:**
    Place this folder in your OpenClaw `skills/` directory.

## Usage

The skill provides a Python script to fetch data.

```bash
# Get yesterday's sleep stats
python3 skills/oura/scripts/oura_api.py sleep 1

# Get activity for the last 7 days
python3 skills/oura/scripts/oura_api.py activity 7

# Check readiness score trends
python3 skills/oura/scripts/oura_api.py readiness 3

# View your profile info
python3 skills/oura/scripts/oura_api.py personal_info
```

## Features

- **Sleep:** Total sleep, efficiency, deep/rem/light breakdown.
- **Activity:** Steps, calories, activity score.
- **Readiness:** HRV balance, resting heart rate, recovery index.
- **Profile:** Basic user info.

## License

MIT
