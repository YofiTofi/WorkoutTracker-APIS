import requests
import datetime
APP_ID = ""
API_KEY = ""
NUT_EP = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_EP = "https://api.sheety.co/54d0ffc33d4058b853cf0d35d8917a89/workoutTracker/workouts"
SHEETY_TOKEN = "Bearer "
SHEETY_ROOT = SHEETY_EP.split("/")[-1]

# nut_signin = {
#     "password": "",
#     "email": "",
# }
nut_header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
nut_params = {
    "query": "",
    "gender": "male",
    "weight_kg": 75,
    "height_cm": 172,
    "age": 25,
}
sheety_headers = {
    "Authorization": SHEETY_TOKEN,
    "Content-Type": "application/json",
}
sheety_data = {
    "Date": "",
    "Time": "",
    "Exercise": "",
    "Duration": "",
    "Calories": "",
}
nut_params["query"] = input("Please describe your workout: ")
nut_response = requests.post(url=NUT_EP, json=nut_params, headers=nut_header)
nut_response.raise_for_status()
print(nut_response.json())
workouts = nut_response.json()["exercises"]
for workout in workouts:
    sheety_data = {
        "workout": {
            "date": datetime.datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.datetime.now().strftime("%H:%M"),
            "exercise": workout["name"],
            "duration": workout["duration_min"],
            "calories": workout["nf_calories"],
        }
    }
    sheety_response = requests.post(url=SHEETY_EP, json=sheety_data, headers=sheety_headers)
    print(sheety_response.text)