import sqlite3


def create_database():
    # connect to the database file (create it if it doesn't exist)
    connect = sqlite3.connect('products.db')
    # create cursor object to execute commands
    cursor = connect.cursor()

    # execute sql to create products table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    # Insert sample data into the Products table
    # This adds two products to get us started
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')

    # save changes to the database file
    connect.commit()
    # close connection to free up resources
    connect.close()

# only run when the file is executed
if __name__ == '__main__':
    create_database()
    print("Database created successfully!")