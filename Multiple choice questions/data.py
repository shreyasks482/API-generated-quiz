import requests

parameters = {
    "amount": 10,
    "type": "multiple",
    "difficulty": "easy",
    "category": "14"
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
