#!/usr/bin/python3
""" CSV  Module
"""
import csv
import requests
from sys import argv as av


if __name__ == '__main__':
    api = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(api + 'users/{}'.format(av[1])).json()
    todo = requests.get(api + 'users/{}/todos'.format(av[1])).json()
    row = [
        [
            av[1],
            user['username'],
            task.get('completed'),
            task.get('title')
        ] for task in todo
    ]
    file = '{}.csv'.format(av[1])
    with open(file, 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(row)
