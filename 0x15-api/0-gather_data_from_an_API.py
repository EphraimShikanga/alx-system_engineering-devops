#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_id = argv[1]
    user = requests.get(url + "/users/{}".format(user_id)).json()
    todo = requests.get(url + "/todos?userId={}".format(user_id)).json()
    completed_tasks = []
    for task in todo:
        if task.get('completed') is True:
            completed_tasks.append(task)
    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'),
        len(completed_tasks),
        len(todo)))
    [print("\t{}".format(task.get("title"))) for task in completed_tasks]
