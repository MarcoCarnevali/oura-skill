# Oura Ring Skill 💍

A skill to fetch sleep, activity, and readiness data from Oura Ring. Designed for AI agents like Codex, Claude Code, and OpenClaw.

## Setup

1.  **Get your Personal Access Token (PAT):**
    - Go to [Oura Cloud › Personal Access Tokens](https://cloud.ouraring.com/personal-access-tokens)
    - Click "Create New Personal Access Token"
    - Give it a name (e.g., `Agent-Skill`)
    - Copy the token string.

2.  **Configure Environment:**
    You have two options:
    
    **Option A: The `.env` File (Recommended)**
    Create a `.env` file in your agent's root directory:
    ```bash
    OURA_ACCESS_TOKEN=your_token_here
    ```

    **Option B: Terminal Export**
    Run this before starting your agent:
    ```bash
    export OURA_ACCESS_TOKEN="your_token_here"
    ```

3.  **Install Skill:**
    Place this folder in your agent's `skills/` directory.

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
