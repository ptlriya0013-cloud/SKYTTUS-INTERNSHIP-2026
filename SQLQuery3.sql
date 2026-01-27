create table employees(
    emp_id int PRIMARY KEY,
    emp_name varchar(50),
    dept_id int,
    salary int
);

insert into employees(emp_id,emp_name, dept_id, salary) values
(1, 'Riya' , 11, 60000),
(2, 'Cheriti' , 12, 45000),
(3, 'Amit', 12, 35000),
(4, 'Tirth', NULL , 35000),
(5, 'Jigar', 12, 30000),
(6, 'Amit', 13 , 40000);

--select * from employees ;

create table departments(
    dept_id int PRIMARY KEY,
    dept_name varchar(50)
);

insert into departments values
(11, 'HR'),
(12, 'Finance'),
(13, 'Marketing');

--select * from departments ;

--drop table departments;

--Display employees name with department name
SELECT e.emp_name, d.dept_name
FROM employees e
JOIN departments d
ON e.dept_id = d.dept_id;

--Display employees earning more than 50000
select * from employees 
where salary > 50000;


--Display department wise total salary
SELECT d.dept_name, SUM(e.salary) AS total_salary
FROM employees e
JOIN departments d
ON e.dept_id = d.dept_id
GROUP BY d.dept_name;


--Display departments with more than 2 employees
SELECT d.dept_name, COUNT(e.emp_id) AS employee_count
FROM employees e
JOIN departments d
ON e.dept_id = d.dept_id
GROUP BY d.dept_name
HAVING COUNT(e.emp_id) > 2;


--Display employees without department
select emp_name 
from employees
where dept_id IS NULL;


