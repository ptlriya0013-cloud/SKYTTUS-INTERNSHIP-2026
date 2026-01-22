CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(30),
    year INT,
    marks INT
);

INSERT INTO students VALUES
(1, 'Riya', 'IT', 3, 87),
(2, 'Cheriti', 'IT', 2, 79),
(3, 'Srushti', 'CSE', 3, 90),
(4, 'Krish', 'ME', 4, 65),
(5, 'Ayaan', 'CSE', 1, 79);


-- Display all records
SELECT * FROM students;


--Display only name and departments
SELECT name, department FROM students;


--Find Students with marks greater than 75
SELECT * FROM students
WHERE marks > 75;


--Display students from CSE department
SELECT * FROM students
WHERE department = 'CSE';


--Sort students by marks (descending)
SELECT * FROM students
ORDER BY marks DESC;

--Display top 3 scorers
SELECT TOP 3 * FROM students
ORDER BY marks DESC

