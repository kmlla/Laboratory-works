# TODO решите задачу
import json

def task() -> float:

    with open('input.json', 'r') as file:
        data = json.load(file)
    dict_sum = sum(i['score'] * i['weight'] for i in data)

    return round(dict_sum, 3)

print(task())
