#!/usr/bin/python3
"""
3-dictionary_of_list_of_dictionaries.py

Exports all TODO tasks for all employees to a single JSON file.
"""

import json
import requests


if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    users = users_response.json()
    todos = todos_response.json()

    usernames_by_id = {}
    for user in users:
        usernames_by_id[user.get("id")] = user.get("username")

    output = {}
    for user in users:
        user_id = str(user.get("id"))
        output[user_id] = []

    for task in todos:
        user_id_int = task.get("userId")
        user_id = str(user_id_int)
        output[user_id].append(
            {
                "username": usernames_by_id.get(user_id_int),
                "task": task.get("title"),
                "completed": task.get("completed")
            }
        )

    with open("todo_all_employees.json", "w", encoding="utf-8") as json_file:
        json.dump(output, json_file)
