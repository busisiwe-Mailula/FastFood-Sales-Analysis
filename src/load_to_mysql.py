import pandas as pd
import mysql.connector

# in this file i will load the cleaned dataset to mysql

# Load cleaned cvs
df = pd.read_csv("data/cleaned/fastfood_sales_clean.csv")


# Load cleaned CSV
df = pd.read_csv("data/cleaned/fastfood_sales_clean.csv")

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="fastfood_user",
    password="fastfood123",
)

cursor = conn.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS fastfood_db")
cursor.execute("USE fastfood_db")

print("Database connected successfully")

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS fastfood_sales (
    order_id INT PRIMARY KEY,
    order_date DATE,
    item_name VARCHAR(50),
    category VARCHAR(50),
    price INT,
    quantity INT,
    payment_method VARCHAR(20),
    revenue INT
)
""")

# Insert data row by row
for _, row in df.iterrows():
    cursor.execute("""
    INSERT IGNORE INTO fastfood_sales
    (order_id, order_date, item_name, category, price, quantity, payment_method, revenue)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""", tuple(row))

# Commit changes
conn.commit()

print("Data loaded successfully!")

cursor.close()
conn.close()
