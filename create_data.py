#The code for loading data into the customer table
#Customer Table
import mysql.connector
from faker import Faker

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

# Generate and insert data
for _ in range(100):  # Let's say we want to generate 100 records
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    phone = fake.phone_number()
    if len(phone) > 20:  # Assuming the 'Phone' column is VARCHAR(20)
        phone = phone[:20]  # Truncate phone number to fit into the column
    address = fake.address()
    customer_since = fake.date_between(start_date='-5y', end_date='today')
    is_active = fake.boolean()
    
    # Insert customer data
    cursor.execute("""
        INSERT INTO Customer (FirstName, LastName, Email, Phone, BillingAddress, ShippingAddress, CustomerSince, IsActive)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (first_name, last_name, email, phone, address, address, customer_since, is_active))

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()