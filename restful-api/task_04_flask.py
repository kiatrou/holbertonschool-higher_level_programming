#!/usr/bin/python3
"""
This is a simple API using Python with Flask
"""


from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)

users = {
    "john": {
        "username":"john",
        "name": "John",
        "age": 30,
        "city": "New York"
    },
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    }
}

@app.route("/")
def home():
    return ("Welcome to the Flask API!")

@app.route("/data")
def return_users():
    usernames = list(users.keys())
    return (jsonify(usernames))

@app.route("/status")
def is_okay():
    return ("OK")

@app.route("/users/<username>")
def lookup_username(username):
    if username in users:
        return (jsonify(users[username]))
    else:
        return (jsonify({"error": "User not found"}), 404)

@app.route("/add_user", methods=['POST'])
def get_data():
    data = request.get_json()
    if not data or "username" not in data:
        return (jsonify({"error": "Username is required"}), 400)

    username = data["username"]
    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201

# this ensures that Flask will only run the sever when
# executing the file directly
if __name__ == "__main__":
    app.run()