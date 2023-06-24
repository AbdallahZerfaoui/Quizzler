import requests


def get_data_question():
    parameters = {
        "amount": 3,
        "category": 23, #18 : computer science , 20 : mythologie 23: History
        "difficulty": "easy",
        "type": "boolean"
    }

    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()

    return response.json()["results"]

