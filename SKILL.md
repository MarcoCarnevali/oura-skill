---
name: oura
description: Access Oura Ring health data. Use to fetch sleep, activity, and readiness scores. Requires OURA_ACCESS_TOKEN env var.
---

# Oura Ring Skill

Use this skill to fetch health metrics from the user's Oura Ring.

## Prerequisites

- `OURA_ACCESS_TOKEN` environment variable must be set with a valid Personal Access Token.

## Commands

### Check recent stats

Run the Python script directly. Defaults to `1` day back (yesterday/today).

```bash
python3 skills/oura/scripts/oura_api.py <command> [days_back]
```

**Commands:**
- `sleep`: Get daily sleep summary (score, total sleep, etc.)
- `activity`: Get daily activity summary (score, steps, calories)
- `readiness`: Get daily readiness summary (score, HRV balance)
- `personal_info`: Get user profile info (no days_back arg needed)

### Examples

**Get yesterday's sleep data:**
```bash
python3 skills/oura/scripts/oura_api.py sleep 1
```

**Get last week's activity:**
```bash
python3 skills/oura/scripts/oura_api.py activity 7
```

**Check readiness trend:**
```bash
python3 skills/oura/scripts/oura_api.py readiness 3
```
