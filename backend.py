from dotenv import load_dotenv
import os
import requests

load_dotenv("B:\\Coding\\Python\\EnviromentVariables\\.env")
OWM_API_KEY = os.getenv("wfa_OWM_API_KEY")


def get_data(location, days=None, data_type=None):
    endpoint = f"https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={OWM_API_KEY}"
    response = requests.get(endpoint)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * days
    filtered_data = filtered_data[:8*nr_values]
    if data == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if data == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data


if __name__ == "__main__":
    get_data(location="London")
