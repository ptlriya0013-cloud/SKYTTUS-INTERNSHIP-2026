-- Count total number of students
SELECT COUNT(*) AS total_students
FROM students;

--FIND AVERAGE MARKS OF STUDENTS
SELECT AVG(marks) AS avg_marks
FROM students;

--Find highest and lowest marks
SELECT 
max(marks) AS "Highest Mark",
min(marks) AS "Lowest Marks" 
FROM students;

--Find Department wise average marks 

SELECT department, AVG (marks)
FROM students
group by department;

--Display departments where average marks >70
SELECT department , avg (marks) AS "avg_marks"
FROM students
group by department
having avg(marks) > 70