#!/usr/bin/python3
""" API Module
"""
import requests
from sys import argv as av


if __name__ == '__main__':
    api = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(api + 'users/{}'.format(av[1])).json()
    todo = requests.get(api + 'users/{}/todos'.format(av[1])).json()
    tasks = [task.get('title') for task in todo if task.get('completed')]
    first_line = 'Employee {} is done with '.format(user['name'])
    first_line += 'tasks({}/{}):'.format(len(tasks), len(todo))

    print(first_line)
    [print('\t {}'.format(task)) for task in tasks]
