#Supplier Table
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

# Generate and insert data into the Supplier table
for _ in range(1000):  # Assuming you want to insert 1000 records
    company_name = fake.company()
    contact_name = fake.name()
    contact_title = fake.job()
    # Ensure ContactTitle does not exceed the column's max length, e.g., VARCHAR(50)
    contact_title = contact_title[:50] if len(contact_title) > 50 else contact_title
    address = fake.address().replace('\n', ', ')  # Replace newlines with commas for address
    phone = fake.phone_number()
    # Ensure phone does not exceed the column's max length, e.g., VARCHAR(20)
    phone = phone[:20] if len(phone) > 20 else phone
    email = fake.email()

    # Insert supplier data
    cursor.execute("""
        INSERT INTO Supplier (CompanyName, ContactName, ContactTitle, Address, Phone, Email)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (company_name, contact_name, contact_title, address, phone, email))

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Suppliers inserted successfully.")