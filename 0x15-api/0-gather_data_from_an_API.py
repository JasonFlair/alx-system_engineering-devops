#!/usr/bin/python3
"""a script that uses an API to return info"""
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]  # take the input employee_id from command line
    todo_url = f"https://jsonplaceholder.typicode.com/" \
               f"todos?userId={employee_id}"
    username_url = f"https://jsonplaceholder.typicode.com/" \
                   f"users/{employee_id}"

    # send a GET request to todo_url and username_url
    # to retrieve the todo and employee data
    to_do_response = requests.get(todo_url)
    employee_response = requests.get(username_url)

    # retrieve the data in json format
    to_do_tasks = to_do_response.json()
    employee_data = employee_response.json()

    # get the name of the employee
    employee_name = employee_data["name"]

    all_tasks = []
    # store all the tasks in all_tasks list
    for task in to_do_tasks:
        all_tasks.append(task)
    total_task_num = len(all_tasks)
    completed_tasks = []
    # store the completed tasks in completed_tasks list
    for task_info in to_do_tasks:
        if task_info.get('completed') is True:
            completed_tasks.append(task_info)
    completed_tasks_num = len(completed_tasks)
    print(f"Employee {employee_name} is done with "
          f"tasks({completed_tasks_num}/{total_task_num}):")
    # print the title of the completed tasks
    for each_task in completed_tasks:
        print(f"\t{each_task['title']}")