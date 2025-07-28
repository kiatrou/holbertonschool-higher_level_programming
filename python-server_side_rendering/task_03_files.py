#!/usr/bin/python3

import json
import csv
from flask import Flask, render_template

app = Flask(__name__)

def read_json_file():
    # Read JSON data from file
    with open('products.json') as f:
        return json.load(f)

def read_csv_file():
    # Read CSV data into a list of dicts
    data = []
    with open('products.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append({
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            })
    return data

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
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
        # Use .get() with default empty list
        items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        # Default to empty list if file issues
        items_list = []

    return render_template('items.html', items=items_list)

@app.route('/products')
def show_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    if source == 'json':
        data = read_json_file()
    elif source == 'csv':
        data = read_csv_file()
    else:
        return render_template('product_display.html', error='Wrong source', products=[])

    if product_id:
        filtered = [prod for prod in data if str(prod.get('id')) == str(product_id)]
        if not filtered:
            return render_template('product_display.html', error='Product not found', products=[])
        return render_template('product_display.html', products=filtered)
    
    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)