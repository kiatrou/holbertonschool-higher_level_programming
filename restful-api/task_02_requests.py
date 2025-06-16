#!/usr/bin/python3
"""
This is a basic script to fetch posts from JSONPlaceholder
"""


import requests
import csv


def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: ", response.status_code)

    if response.status_code == 200:
        data = response.json()  # convert response to JSON (a list of posts)
        for post in data:
            print(post["title"])  # print each title


def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        data = response.json()

        # Only keep id, title, and body
        posts = [{"id": post["id"], "title": post["title"],
                  "body": post["body"]} for post in data]

        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts)
