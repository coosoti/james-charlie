#!/usr/bin/python3
"""From API. 0. Gather data from an API.
Return information about an employee based
on id."""
import requests
import sys


if __name__ == "__main__":
    resp = (
        requests
        .get(
            'https://jsonplaceholder.typicode.com/todos',
            params={"userId": sys.argv[1]}
            )
        ).json()
    user = (
        requests
        .get(
            'https://jsonplaceholder.typicode.com/users/{}'
            . format(sys.argv[1])
            )
        ).json()
    done = [i.get('title') for i in resp if i.get('completed') is True]
    print(
        "Employee {} is done with tasks({}/{}):"
        .format(user.get('name'), len(done), len(resp)))
    for tsk in done:
        print("     {}".format(tsk))
