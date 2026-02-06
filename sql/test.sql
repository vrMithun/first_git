create database mysql_java;
use mysql_java;
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department_id INT,
    salary DECIMAL(10, 2),
    hire_date DATE
);

INSERT INTO employees (employee_id, first_name, last_name, department_id, salary, hire_date) 
VALUES 
(1, 'John', 'Doe', 10, 5000.00, '2015-06-01'),
(2, 'Jane', 'Smith', 20, 6500.00, '2017-03-15'),
(3, 'Alice', 'Johnson', 10, 4500.00, '2018-09-25'),
(4, 'Bob', 'Brown', 30, 7000.00, '2016-11-20'),
(5, 'Charlie', 'Davis', 20, 8000.00, '2014-05-10'),
(6, 'Diana', 'Miller', 40, 6000.00, '2019-07-01'),
(7, 'Edward', 'Wilson', 30, 5500.00, '2020-10-30'),
(8, 'Fiona', 'Clark', 40, 9000.00, '2013-01-17'),
(9, 'George', 'White', 10, 4800.00, '2016-02-28'),
(10, 'Hannah', 'Walker', 20, 7200.00, '2015-11-11');
