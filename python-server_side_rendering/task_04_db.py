#!/usr/bin/python3

import json
import csv
import sqlite3
from flask import Flask, render_template, request

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
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return data

def read_sqlite_file():
    # read data from SQLite database
    data = []
    try:
        connect = sqlite3.connect('products.db')
        cursor = connect.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        row = cursor.fetchall()

        for row in row:
            data.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        connect.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

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
    # get json or csv file
    source = request.args.get('source')
    # get the id number
    product_id = request.args.get('id')

    # check if source is valid
    if source not in ['json', 'csv', 'sql']:
        print("Error: Wrong source")
        return render_template('product_display.html', error="Wrong source")

    # read from json file else from csv file
    if source == 'json':
        products = read_json_file()
    elif source == 'csv':
        products = read_csv_file()
    else:
        products = read_sqlite_file()

    # find product with id else return error
    if product_id:
        try:
            product_id = int(product_id)  # Convert to integer
            # Filter products to find the one with matching ID
            matching_products = [p for p in products if p['id'] == product_id]
            
            if not matching_products:
                return render_template('product_display.html', error="Product not found")
            
            products = matching_products  # Only show the matching product
        except ValueError:
            return render_template('product_display.html', error="Invalid ID format")

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)