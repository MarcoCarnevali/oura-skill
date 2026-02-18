#!/usr/bin/env python3
import os
import sys
import json
import datetime
import urllib.request
import urllib.error
import urllib.parse

# Configuration
API_BASE = "https://api.ouraring.com/v2/usercollection"
TOKEN = os.environ.get("OURA_ACCESS_TOKEN")

def get_headers():
    if not TOKEN:
        print("❌ Error: OURA_ACCESS_TOKEN environment variable is missing.")
        print("\nTo fix this:")
        print("1. Go to https://cloud.ouraring.com/personal-access-tokens")
        print("2. Generate a new Personal Access Token.")
        print("3. Set the environment variable using one of these methods:")
        print("   - Option A (Recommended): Create a .env file in your agent's root directory with:\n     OURA_ACCESS_TOKEN=your_token_here")
        print("   - Option B: Add to your shell config (~/.zshenv, ~/.bashrc):\n     echo 'export OURA_ACCESS_TOKEN=\"your_token_here\"' >> ~/.zshenv\n     source ~/.zshenv")
        print("   - Option C: Export temporarily in your terminal:\n     export OURA_ACCESS_TOKEN='your_token_here'")
        sys.exit(1)
    return {
        "Authorization": f"Bearer {TOKEN}"
    }

def fetch_data(endpoint, start_date=None, end_date=None):
    params = {}
    if start_date:
        params['start_date'] = start_date
    if end_date:
        params['end_date'] = end_date
    
    query_string = urllib.parse.urlencode(params)
    url = f"{API_BASE}/{endpoint}"
    if query_string:
        url += f"?{query_string}"

    try:
        req = urllib.request.Request(url, headers=get_headers())
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                return json.loads(response.read().decode())
            else:
                print(f"Error: API returned status {response.status}")
                sys.exit(1)
    except urllib.error.HTTPError as e:
        print(f"Error fetching data: {e}")
        print(e.read().decode())
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def get_advice(readiness_data, sleep_data):
    if not readiness_data['data'] or not sleep_data['data']:
        return "Not enough data to generate advice."

    # Get latest entries
    r = readiness_data['data'][-1]
    s = sleep_data['data'][-1]
    
    r_score = r.get('score', 0)
    s_score = s.get('score', 0)
    
    # Analyze
    status = "UNKNOWN"
    advice = ""
    
    if r_score >= 85:
        status = "PEAK PERFORMANCE 🚀"
        advice = "Your body is ready for high-intensity work. Push your limits today."
    elif r_score >= 70:
        status = "OPTIMAL 🟢"
        advice = "Good recovery. Maintain normal training and workload."
    else:
        status = "RECOVERY MODE 🔴"
        advice = "Your body is stressed. Prioritize light movement, nap, and early sleep."

    if s_score < 60:
        advice += "\n⚠️ Warning: Sleep score is critically low. Cognitive function may be impaired."

    return json.dumps({
        "status": status,
        "advice": advice,
        "scores": {
            "readiness": r_score,
            "sleep": s_score
        },
        "date": r.get('day')
    }, indent=2)

def main():
    if len(sys.argv) < 2:
        print("Usage: oura_api.py <command> [days_back]")
        print("Commands: sleep, activity, readiness, personal_info, advise")
        sys.exit(1)

    command = sys.argv[1]
    days_back = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    
    today = datetime.date.today()
    start_date = (today - datetime.timedelta(days=days_back)).isoformat()
    end_date = today.isoformat()

    if command == "personal_info":
        data = fetch_data("personal_info")
        print(json.dumps(data, indent=2))
        return

    if command == "advise":
        # Need both readiness and sleep
        r_data = fetch_data("daily_readiness", start_date, end_date)
        s_data = fetch_data("daily_sleep", start_date, end_date)
        print(get_advice(r_data, s_data))
        return

    endpoint_map = {
        "sleep": "daily_sleep",
        "activity": "daily_activity",
        "readiness": "daily_readiness"
    }

    if command not in endpoint_map:
        print(f"Unknown command: {command}")
        sys.exit(1)

    data = fetch_data(endpoint_map[command], start_date, end_date)
    print(json.dumps(data, indent=2))

if __name__ == "__main__":
    main()
