#Employee Table
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

# Generate and insert 1000 employee records
for _ in range(1000):
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    phone = fake.phone_number()
    if len(phone) > 20:  # Truncate phone number if necessary
        phone = phone[:20]
    hire_date = fake.date_between(start_date='-5y', end_date='today')
    position = fake.job()
    salary = round(fake.random_number(digits=5), 2)  # Generate a 5 digit salary
    
    # Insert employee data
    cursor.execute("""
        INSERT INTO Employee (FirstName, LastName, Email, Phone, HireDate, Position, Salary)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (first_name, last_name, email, phone, hire_date, position, salary))

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("1000 employee records inserted successfully.")