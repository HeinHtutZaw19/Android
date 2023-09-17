import csv
import random
from faker import Faker

# List of courses
courses = [
    ("POL 101", 206304981),
    ("POL 102", 202960353),
    ("WRT 101", 209038933),
    ("WRT 102", 203065551),
    ("CSE 114", 207160222),
    ("CSE 115", 205981170),
    ("CSE 214", 203564191),
    ("CSE 220", 203184775),
    ("CSE 216", 203488947),
    ("CSE 303", 204547399),
    ("CSE 327", 209567223),
    ("CSE 310", 202323245),
    ("CSE 337", 202368382),
    ("CSE 316", 201432297),
    ("CSE 320", 206386697),
    ("CSE 416", 209587427),
    ("AMS 151", 204774701),
    ("AMS 161", 204282394),
    ("AMS 210", 205304498),
    ("AMS 301", 202659154),
    ("AMS 355", 202757189),
    ("AMS 216", 208588576),
    ("CSE 101", 202349695),
    ("SOC 101", 204605776),
    ("SOC 102", 204745793),
    ("FLM 102", 203188263),
    ("FLM 101", 203783312),
    ("WAE 146", 206442900),
    ("EST 220", 203204228),
    ("EST 216", 205098103),
    ("EST 300", 208873696),
    ("ESS 131", 209755368),
    ("EST 214", 203687077),
    ("EST 316", 204275261),
    ("ESS 310", 205721057),
    ("ISE 327", 203169821),
    ("ISE 373", 209129341)
]

fake = Faker()

# Function to generate a unique ID
def generate_unique_id(existing_ids):
    new_id = None
    while new_id is None or new_id in existing_ids:
        new_id = f"11{random.randint(1000000, 9999999)}"
    return new_id

# Function to generate a unique email with incremented numbers
def generate_unique_email(existing_emails, base_email):
    new_email = base_email
    counter = 1
    while new_email in existing_emails:
        new_email = f"{base_email}{counter}"
        counter += 1
    return new_email

class Student:
    def __init__(self, id, name, email):
        self.name = name
        self.id = id
        self.email = email
        self.enrolled_courses = []

# Generate data for the CSV files
existing_ids = set()
existing_emails = set()
students = []

# Create data for 10 students
for _ in range(10):
    unique_id = generate_unique_id(existing_ids)
    name = fake.name()
    base_email = f"{name.replace(' ', '.').lower()}@stonybrook.edu"
    unique_email = generate_unique_email(existing_emails, base_email)
    students.append(Student(unique_id, name, unique_email))

# Shuffle the list of courses
random.shuffle(courses)

# Specify the absolute path for the export directory
export_directory = "..\\spreadsheet"

for course_name, class_id in courses:
    data = []

    # Randomly select up to 5 students for each class (if they haven't reached the limit)
    for student in students:
        if len(student.enrolled_courses) < 5 and random.random() < 0.5:
            student.enrolled_courses.append(course_name)

            # Generate data for Fall 2023 semester
            semester = "Fall 2023"
            class_name = course_name
            attendance = random.randint(0, 100)
            participation = random.randint(0, 100)
            recitation = random.randint(0, 100)
            presentation = random.randint(0, 100)
            project = random.randint(0, 100)
            midterm1 = random.randint(0, 100)
            midterm2 = random.randint(0, 100)
            midterm3 = random.randint(0, 100)
            finals = random.randint(0, 100)
            assignment1 = random.randint(0, 100)
            assignment2 = random.randint(0, 100)
            assignment3 = random.randint(0, 100)
            assignment4 = random.randint(0, 100)
            quiz1 = random.randint(0, 100)
            quiz2 = random.randint(0, 100)
            quiz3 = random.randint(0, 100)
            quiz4 = random.randint(0, 100)

            data.append([student.id, student.name, student.email, semester, class_id, class_name, attendance, participation, recitation,
                         presentation, project, midterm1, midterm2, midterm3, finals, assignment1, assignment2, assignment3,
                         assignment4, quiz1, quiz2, quiz3, quiz4])

    # Write data to a CSV file in the specified export directory (if there is data)
    if data:
        filename = f"{export_directory}\\{course_name}_student_data.csv"
        with open(filename, "w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["id", "name", "email", "semester", "class_id", "class_name", "attendance", "participation", "recitation",
                                 "presentation", "project", "midterm1", "midterm2", "midterm3", "finals", "assignment1", "assignment2",
                                 "assignment3", "assignment4", "quiz1", "quiz2", "quiz3", "quiz4"])
            csv_writer.writerows(data)

        print(f"CSV file '{filename}' has been generated.")

# Print out student names and their enrolled courses
for student in students:
    print(f"Student Name: {student.name}")
    print("Enrolled Courses:")
    for course in student.enrolled_courses:
        print(course)
    print()
