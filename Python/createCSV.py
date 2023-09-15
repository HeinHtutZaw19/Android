import csv
import random
from faker import Faker

# List of courses
courses = ["POL 101", "POL 102", "WRT 101", "WRT 102", "CSE 114", "CSE 115", "CSE 214", "CSE 220",
           "CSE 216", "CSE 303", "CSE 327", "CSE 373", "CSE 310", "CSE 337", "CSE 416", "CSE 316", "CSE 320",
           "AMS 151", "AMS 161", "AMS 210", "AMS 301", "AMS 310", "AMS 355", "AMS 216", "CSE 101", "SOC 102",
           "FLM 102", "FLM 101", "SOC 101", "WAE 146", "EST 220", "EST 216", "EST 300", "ESS 131", "EST 214",
           "EST 216", "EST 316", "ESS 310", "ISE 327", "ISE 373"]

fake = Faker()

# Function to generate a unique ID
def generate_unique_id(existing_ids):
    new_id = None
    while new_id is None or new_id in existing_ids:
        new_id = f"11{random.randint(1000000, 9999999)}"
    return new_id

# Function to generate unique email with incremented numbers
def generate_unique_email(existing_emails, base_email):
    new_email = base_email
    counter = 1
    while new_email in existing_emails:
        new_email = f"{base_email}{counter}"
        counter += 1
    return new_email

# Generate data for the CSV file
data = []
existing_ids = set()
existing_emails = set()

for _ in range(100):  # You can adjust the number of entries as needed
    unique_id = generate_unique_id(existing_ids)
    name = fake.name()
    base_email = f"{name.replace(' ', '.').lower()}@stonybrook.edu"
    unique_email = generate_unique_email(existing_emails, base_email)

    # Generate data for three semesters
    for semester in ["Spring 2023", "Fall 2022", "Spring 2022"]:
        course_selection = random.sample(courses, 5)
        data.append([unique_id, name, unique_email, semester, *course_selection])

    existing_ids.add(unique_id)
    existing_emails.add(unique_email)

# Write data to a CSV file
with open("student_data.csv", "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["id", "name", "email", "semester", "course1", "course2", "course3", "course4", "course5"])
    csv_writer.writerows(data)

print("CSV file 'student_data.csv' has been generated.")
