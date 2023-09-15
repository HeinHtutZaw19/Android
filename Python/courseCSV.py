import csv
import random
from faker import Faker

fake = Faker()

# List of courses with class codes and titles
course_info = [
    ("POL 101", "World Politics"),
    ("POL 102", "Introduction to American Government"),
    ("WRT 101", "Introductory Writing Workshop"),
    ("WRT 102", "Intermediate Writing Workshop"),
    ("CSE 114", "Introduction to Object-Oriented Programming"),
    ("CSE 115", "Introduction to Programming in C"),
    ("CSE 214", "Data Structures"),
    ("CSE 220", "Systems Fundamentals I"),
    ("CSE 216", "Programming Abstractions"),
    ("CSE 303", "Introduction to the Theory of Computation"),
    ("CSE 327", "Fundamentals of Computer Vision"),
    ("CSE 310", "Computer Networks"),
    ("CSE 337", "Scripting Languages"),
    ("CSE 316", "Fundamentals of Software Development"),
    ("CSE 320", "Systems Fundamentals II"),
    ("CSE 416", "Software Engineering"),
    ("AMS 151", "Applied Calculus I"),
    ("AMS 161", "Applied Calculus II"),
    ("AMS 210", "Applied Linear Algebra"),
    ("AMS 310", "Survey of Probability and Statistics"),
    ("AMS 355", "Applied Algebra"),
    ("AMS 216", "Applied Calculus III"),
    ("CSE 101", "Computer Science Principles"),
    ("SOC 101", "Introduction to Sociology"),
    ("SOC 102", "Medicine and Society"),
    ("FLM 102", "Introduction to Film and Television Composition: How Films and TV Shows Say What They Mean"),
    ("FLM 101", "Introduction to Filmmaking and Television: Visual Storytelling"),
    ("WAE 146", "Basic Writing"),
    ("EST 220", "Multimedia for Online Content Platforms"),
    ("EST 216", "Emerging Technologies in Atypical Operations"),
    ("EST 300", "Communication for Engineers and Scientists"),
    ("ESS 131", "Applications Software for Information Management"),
    ("EST 214", "Visual Rhetoric and Information Technology"),
    ("EST 216", "Fundamentals of Industrial Engineering"),
    ("ESS 310", "Design of Computer Games"),
    ("EST 316", "Communication Technology Systems"),
    ("ISE 327", "Database"),
    ("ISE 373", "Hardware Engineering")
]

# Function to generate a unique ID
def generate_unique_id(existing_ids, prefix):
    new_id = None
    while new_id is None or new_id in existing_ids:
        new_id = f"{prefix}{random.randint(1000000, 9999999)}"
    return new_id

# Generate data for the second CSV file
data2 = []
existing_class_names = {}
existing_ta_ids = set()

for course_code, course_title in course_info:
    class_id = generate_unique_id(existing_ta_ids, "20")
    class_name = course_code
    marking_categories_names = ["attendance", "participation", "recitation", "presentation", "project", "midterm1", "midterm2", "midterm3",
                          "finals", "assignments","quizzes", "assignments_count", "quizzes_count"]
    marking_categories = ["attendance", "participation", "recitation", "presentation", "project", "midterm1", "midterm2", "midterm3",
                          "finals", "assignments","quizzes", "assignments_count", "quizzes_count"]
    
    # Calculate assignment and quiz percentages
    marking_categories[9] = random.randint(15, 20)
    marking_categories[10] = random.randint(15, 20)
    marking_categories[11]=random.randint(5,10)
    marking_categories[12]=random.randint(5,10)
    remaining_percentage = 100 - (marking_categories[9] + marking_categories[10])
    
    # Update the marking categories with integer percentages
    for i in range(8):       
        marking_categories[i] = random.randint(0, (int)(remaining_percentage/5))
        remaining_percentage = remaining_percentage-marking_categories[i]
    
    marking_categories[8] = remaining_percentage

    class_time = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=None).strftime("%I:%M %p")
    class_days = fake.random_elements(elements=("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"), length=3, unique=True)
    lecturer_id = generate_unique_id(existing_ta_ids, "11")
    lecturer_name = fake.name()
    lecturer_email = lecturer_name.replace(' ', '.').lower() + "@stonybrook.edu"
    lecturer_office_hours = fake.random_element(elements=("Monday 2-4 PM", "Wednesday 10 AM-12 PM", "Friday 3-5 PM"))
    lecturer_office = fake.random_element(elements=("Office A", "Office B", "Office C"))
    lecturer_phone = fake.phone_number()
    ta_count = random.randint(1, 5)

    if class_name in existing_class_names:
        if existing_class_names[class_name] < 2:
            existing_class_names[class_name] += 1
        else:
            continue
    else:
        existing_class_names[class_name] = 1

    for _ in range(ta_count):
        ta_id = generate_unique_id(existing_ta_ids, "11")
        ta_name = fake.name()
        ta_email = ta_name.replace(' ', '.').lower() + "@stonybrook.edu"
        ta_office_hours = fake.random_element(elements=("Monday 2-4 PM", "Wednesday 10 AM-12 PM", "Friday 3-5 PM"))
        ta_office = fake.random_element(elements=("Office A", "Office B", "Office C"))

        data2.append([class_id, class_name, course_title,
                    marking_categories[0], marking_categories[1], marking_categories[2], marking_categories[3], marking_categories[4], marking_categories[5],
                    marking_categories[6], marking_categories[7], marking_categories[8], marking_categories[9], marking_categories[10],marking_categories[11],marking_categories[12],
                    class_time, ", ".join(class_days),
                     lecturer_id, lecturer_name, lecturer_email, lecturer_office_hours, lecturer_office, lecturer_phone,
                     ta_count, ta_id, ta_name, ta_email, ta_office_hours, ta_office])

    existing_ta_ids.add(class_id)

# Write data to the second CSV file
with open("class_data.csv", "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["class_id", "class_name", "course_title", *marking_categories_names, "class_time", "class_days",
                         "lecturer_id", "lecturer_name", "lecturer_email", "lecturer_office_hours", "lecturer_office", "lecturer_phone",
                         "ta_count", "ta_id", "ta_name", "ta_email", "ta_office_hours", "ta_office"])
    csv_writer.writerows(data2)

print("CSV file 'class_data.csv' has been generated.")
