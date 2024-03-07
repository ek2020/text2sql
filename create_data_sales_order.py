#Sales Order Table
import mysql.connector
from faker import Faker
from datetime import timedelta
import random

fake = Faker()

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="SalesOrderSchema"
)
cursor = conn.cursor(buffered=True)

# Fetch customer IDs
cursor.execute("SELECT CustomerID FROM Customer")
customer_ids = [id[0] for id in cursor.fetchall()]

# Insert data into SalesOrder
for _ in range(1000):  # Let's say we want to generate 1000 sales orders
    customer_id = random.choice(customer_ids)
    order_date = fake.date_between(start_date='-2y', end_date='today')
    required_date = order_date + timedelta(days=random.randint(1, 30))
    shipped_date = order_date + timedelta(days=random.randint(1, 30)) if random.choice([True, False]) else None
    status = random.choice(['Pending', 'Completed', 'Shipped'])
    is_paid = random.choice([True, False])

    cursor.execute("""
        INSERT INTO SalesOrder (CustomerID, OrderDate, RequiredDate, ShippedDate, Status, IsPaid)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (customer_id, order_date, required_date, shipped_date, status, is_paid))

conn.commit()