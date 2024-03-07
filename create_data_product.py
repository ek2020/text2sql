#Product Table
import mysql.connector
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Connect to MySQL
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="SalesOrderSchema"
)
cursor = conn.cursor()

# Generate and insert data into the Product table
for _ in range(1000):  # Generate 1000 product records
    product_name = fake.word().capitalize() + " " + fake.word().capitalize()
    description = fake.sentence(nb_words=10)
    unit_price = round(random.uniform(10, 500), 2)  # Random price between $10 and $500
    stock_quantity = random.randint(10, 1000)  # Random stock quantity between 10 and 1000
    reorder_level = random.randint(5, 50)  # Random reorder level between 5 and 50
    discontinued = random.choice([0, 1])  # Randomly choose between 0 (false) and 1 (true)

    # Insert product data
    cursor.execute("""
        INSERT INTO Product (ProductName, Description, UnitPrice, StockQuantity, ReorderLevel, Discontinued)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (product_name, description, unit_price, stock_quantity, reorder_level, discontinued))

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Products inserted successfully.")