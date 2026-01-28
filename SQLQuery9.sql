--ASSESSMENT 9 -SQL Coding Testing
CREATE TABLE employee (
    emp_id INT,
    emp_name VARCHAR(50),
    salary INT,
    hire_date DATE
);


INSERT INTO employee (emp_id, emp_name,salary, hire_date) VALUES 
(1, 'Riya',   50000, '2024-08-10'),
(2, 'Amit',   60000, '2024-10-15'),
(3, 'Krish',  70000, '2025-01-05'),
(4, 'Riya',   50000, '2024-08-10'), 
(5, 'Neha',   65000, '2025-09-12'),
(6, 'Amit',   60000, '2024-10-15'); 

SELECT * FROM employee;


--Write query ti find Nth highest salary  (Example: 3rd highest)
SELECT DISTINCT salary
FROM employee e1
WHERE 2 = (
    SELECT COUNT(DISTINCT salary)
    FROM employee e2
    WHERE e2.salary > e1.salary
);




--Remove duplicates records
WITH cte AS (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY emp_name, salary
               ORDER BY emp_id
           ) AS rn
    FROM employee
)
DELETE FROM cte
WHERE rn > 1;

SELECT * FROM employee;

--Find records common in two tables
CREATE TABLE employees_old (
    emp_id INT,
    emp_name VARCHAR(50)
);

INSERT INTO employees_old VALUES
(1, 'Riya'),
(2, 'Amit'),
(3, 'Krish'),
(4, 'Neha');

SELECT * FROM employees_old;


CREATE TABLE employees_new (
    emp_id INT,
    emp_name VARCHAR(50)
);


INSERT INTO employees_new VALUES
(3, 'Krish'),
(4, 'Neha'),
(5, 'Ayaan'),
(6, 'Riya');

SELECT * FROM employees_new;


--Find employees hired in last 6 months
SELECT *
FROM employee
WHERE hire_date >= DATEADD(MONTH, -6, GETDATE());


--Find continuous duplicate values
CREATE TABLE logs (
    id INT,
    value INT
);

INSERT INTO logs VALUES
(1, 100),
(2, 100),
(3, 200),
(4, 300),
(5, 300),
(6, 300),
(7, 400);

SELECT * FROM logs;