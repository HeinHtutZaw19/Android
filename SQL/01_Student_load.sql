CREATE TABLE student(
    id INTEGER UNIQUE,
    name VARCHAR(128),
    mail VARCHAR(128)UNIQUE,
    PRIMARY KEY(id)
);
CREATE TABLE lecturer(
    id INTEGER UNIQUE,
    name VARCHAR(128),
    mail VARCHAR(128) UNIQUE,
    office_hours_start VARCHAR(128),
    office_hours_end VARCHAR(128),
    office VARCHAR(128),
    phone VARCHAR(128),
    office_hours_days VARCHAR(128)
);
CREATE TABLE course(
    id INTEGER UNIQUE,
    name VARCHAR(128),
    time_start TIME,
    time_finish TIME,
    place VARCHAR(128),
    schedule VARCHAR(128),
    attendance INTEGER,
    participation INTEGER,
    recitation INTEGER,
    presentation INTEGER,
    project INTEGER,
    midterm INTEGER[],
    final INTEGER,
    lecturer_id INTEGER REFERENCES lecturer(id) ON DELETE CASCADE,
    assignment INTEGER,
    assignment_count INTEGER,
    quiz INTEGER,
    quiz_count INTEGER,
    PRIMARY KEY(id)
);
CREATE TABLE TA(
    id INTEGER UNIQUE,
    name VARCHAR(128),
    mail VARCHAR(128) UNIQUE,
    office_hours_start TIME,
    office_hours_end TIME,
    course_id INTEGER REFERENCES course(id) ON DELETE CASCADE,
    PRIMARY KEY(id)
    office VARCHAR(128),
    office_hours_days VARCHAR(128)
);
CREATE TABLE course_member (
    student_id INTEGER,
    course_id INTEGER,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES student(id),
    FOREIGN KEY (course_id) REFERENCES course(id)
);

CREATE TABLE marks (
    student_id INTEGER,
    course_id INTEGER,
    attendance INTEGER,
    participation INTEGER,
    recitation INTEGER,
    presentation INTEGER,
    project INTEGER,
    midterm INTEGER[],
    final INTEGER,
    assignment INTEGER[],
    quiz INTEGER[],
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id, course_id) REFERENCES course_member(student_id, course_id)
);

INSERT INTO student(id,name,mail) VALUES ('115344093', 'Hein Htut Zaw', 'Hein.Zaw@stonybrook.edu');
INSERT INTO student(id,name,mail) VALUES ('114960520', 'Thazin Pwint Aung', 'Thazin.Aung@stonybrook.edu');


INSERT INTO lecturer(id,name,mail,office_hours_start,office_hours_end,office,phone,office_hours_days) VALUES('000000', 'Lori Scarlatos', 'lori.scarlatos@stonybrook.edu','04:00,11:30am','5:30pm (online),1:00pm (face to face or online)', '1413 Computer Science', '631-632-8761', 'Monday, Thursday');
-- Inserting the first lecturer
INSERT INTO lecturer (id, name, mail, office_hours_start, office_hours_end, office, phone, office_hours_days)
VALUES ('000001', 'John Doe', 'john.doe@example.com', '04:00 AM', '11:30 AM', 'Room 101', '123-456-7890', 'Monday, Wednesday');

-- Inserting the second lecturer
INSERT INTO lecturer (id, name, mail, office_hours_start, office_hours_end, office, phone, office_hours_days)
VALUES ('000002', 'Jane Smith', 'jane.smith@example.com', '02:00 PM', '05:30 PM', 'Room 202', '987-654-3210', 'Tuesday, Thursday');

-- Inserting the third lecturer
INSERT INTO lecturer (id, name, mail, office_hours_start, office_hours_end, office, phone, office_hours_days)
VALUES ('000003', 'Bob Johnson', 'bob.johnson@example.com', '09:00 AM', '12:00 PM', 'Room 303', '555-123-4567', 'Monday, Friday');

-- Inserting the fourth lecturer
INSERT INTO lecturer (id, name, mail, office_hours_start, office_hours_end, office, phone, office_hours_days)
VALUES ('000004', 'Alice Brown', 'alice.brown@example.com', '01:00 PM', '04:00 PM', 'Room 404', '777-888-9999', 'Wednesday, Thursday');

-- Inserting the fifth lecturer
INSERT INTO lecturer (id, name, mail, office_hours_start, office_hours_end, office, phone, office_hours_days)
VALUES ('000005', 'Eva Green', 'eva.green@example.com', '10:00 AM', '01:30 PM', 'Room 505', '111-222-3333', 'Tuesday, Friday');
-- Inserting the first TA with a unique ID starting with "11"
INSERT INTO ta (id, name, mail, course_id, office_hours_start, office_hours_end, office, office_hours_days)
VALUES (
    115344093,  -- Unique ID starting with "11"
    'TA John',
    'ta.john@stonybrook.edu',
    1,
    '09:00 AM',
    '11:00 AM',
    'Room 101',
    'Monday, Wednesday'
);

-- Inserting the second TA with a unique ID starting with "11"
INSERT INTO ta (id, name, mail, course_id, office_hours_start, office_hours_end, office, office_hours_days)
VALUES (
    115344094,  -- Unique ID starting with "11"
    'TA Jane',
    'ta.jane@stonybrook.edu',
    2,
    '02:00 PM',
    '04:00 PM',
    'Room 202',
    'Tuesday, Thursday'
);

-- Inserting the third TA with a unique ID starting with "11"
INSERT INTO ta (id, name, mail, course_id, office_hours_start, office_hours_end, office, office_hours_days)
VALUES (
    115344095,  -- Unique ID starting with "11"
    'TA Bob',
    'ta.bob@stonybrook.edu',
    3,
    '10:00 AM',
    '12:00 PM',
    'Room 303',
    'Monday, Friday'
);

-- Inserting the fourth TA with a unique ID starting with "11"
INSERT INTO ta (id, name, mail, course_id, office_hours_start, office_hours_end, office, office_hours_days)
VALUES (
    115344096,  -- Unique ID starting with "11"
    'TA Alice',
    'ta.alice@stonybrook.edu',
    4,
    '01:00 PM',
    '03:00 PM',
    'Room 404',
    'Wednesday, Thursday'
);

-- Inserting the fifth TA with a unique ID starting with "11"
INSERT INTO ta (id, name, mail, course_id, office_hours_start, office_hours_end, office, office_hours_days)
VALUES (
    115344097,  -- Unique ID starting with "11"
    'TA Eva',
    'ta.eva@stonybrook.edu',
    5,
    '11:00 AM',
    '01:00 PM',
    'Room 505',
    'Tuesday, Friday'
);

-- Inserting the sixth TA with a unique ID starting with "11"
INSERT INTO ta (id, name, mail, course_id, office_hours_start, office_hours_end, office, office_hours_days)
VALUES (
    115344098,  -- Unique ID starting with "11"
    'TA Mark',
    'ta.mark@stonybrook.edu',
    4,
    '08:00 AM',
    '10:00 AM',
    'Room 606',
    'Monday, Wednesday'
);

-- Inserting the seventh TA with a unique ID starting with "11"
INSERT INTO ta (id, name, mail, course_id, office_hours_start, office_hours_end, office, office_hours_days)
VALUES (
    115344099,  -- Unique ID starting with "11"
    'TA Sarah',
    'ta.sarah@stonybrook.edu',
    5,
    '03:00 PM',
    '05:00 PM',
    'Room 707',
    'Tuesday, Thursday'
);

SELECT student.name,course.attendance,marks.attendance
FROM student
JOIN course_member ON course_member.student_id=student.id
JOIN course ON course_member.course_id =course.id
JOIN lecturer ON lecturer.id=course.lecturer_id
JOIN ta ON ta.course_id=course.id
JOIN marks ON course_member.course_id= marks.course_id AND course_member.student_id = marks.student_id;
