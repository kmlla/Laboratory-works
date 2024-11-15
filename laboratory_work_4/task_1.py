# TODO решите задачу
import json

def task() -> float:

    with open('input.json', 'r') as file:
        data = json.load(file)

    dict_sum = 0
    for i in data:
        dict_sum += i['score'] * i['weight']

    return round(dict_sum, 3)

print(task())
