import json
import requests

def get_text():
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        people_info = data.get('people', [])
        result = {
            "total_astronauts": data.get("number", 0),
            "astronauts_in_space": [{"name": person["name"], "spaceship": person["craft"]} for person in people_info],
            "message": data.get("message", "No message available"),
            "timestamp": data.get("timestamp", "Not available")
        }
        print(json.dumps(result, indent=4))
    else:
        print("Error")
get_text()
