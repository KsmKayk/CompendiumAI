import json


def generate_book(data):
    try:
        data = json.loads(data)

        if "topic" not in data or "target_audience" not in data:
            return {"error": "You must provide a topic and a target_audience"}

        return data

    except:
        return {"error": "Invalid JSON"}
