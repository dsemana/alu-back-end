#!/usr/bin/python3
"""
1-export_to_CSV.py

Exports all TODO tasks for a given employee to a CSV file.
"""

import csv
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

    file_name = "{}.csv".format(employee_id)
    with open(file_name, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(
            csv_file,
            delimiter=",",
            quotechar='"',
            quoting=csv.QUOTE_ALL,
            lineterminator="\n"
        )
        for task in todos:
            writer.writerow(
                [
                    employee_id,
                    username,
                    task.get("completed"),
                    task.get("title")
                ]
            )
