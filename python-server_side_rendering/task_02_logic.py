#!/usr/bin/python3

import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    # Open and read json file (opens JSON file for reading)
    with open('items.json', 'r') as file:
        # converst the JSON into a Python dictionary
        data = json.load(file)
    # extract the items list from the data (gets the value of the "items" key from JSON - which is the list)
    items_list = data['items']
    # pass it to the template (passes that list to the template)
    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)