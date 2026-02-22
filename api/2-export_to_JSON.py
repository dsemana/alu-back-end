#!/usr/bin/python3
"""
2-export_to_JSON.py

Exports all TODO tasks for a given employee to a JSON file.
"""

import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = sys.argv[1]

    user_url = (
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    )
    todos_url = (
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            employee_id
        )
    )

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user = user_response.json()
    todos = todos_response.json()
    username = user.get("username")

    tasks = []
    for task in todos:
        tasks.append(
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
        )

    output = {employee_id: tasks}

    file_name = "{}.json".format(employee_id)
    with open(file_name, "w", encoding="utf-8") as json_file:
        json.dump(output, json_file)
