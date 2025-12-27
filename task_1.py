# TODO решите задачу
import json

def task() -> float:
    with open('input.json') as f:
        return round(sum(item["score"] * item["weight"] for item in json.load(f)), 3)

print(task())
