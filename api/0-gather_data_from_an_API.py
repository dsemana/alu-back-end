#!/usr/bin/python3
"""
0-gather_data_from_an_API.py

Fetches and displays the TODO list progress of a given employee
using the JSONPlaceholder REST API.
"""

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

    if user_response.status_code != 200:
        sys.exit(1)

    user = user_response.json()
    todos = todos_response.json()

    employee_name = user.get("name")
    total_tasks = len(todos)

    done_tasks = []
    for task in todos:
        if task.get("completed") is True:
            done_tasks.append(task)

    number_of_done_tasks = len(done_tasks)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name,
            number_of_done_tasks,
            total_tasks
        )
    )

    for task in done_tasks:
        print("\t {}".format(task.get("title")))