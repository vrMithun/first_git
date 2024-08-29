CREATE TABLE Students (
    id INT(5),
    name VARCHAR(20),
    age INT(3)
);

-- 2. Insert into Table
INSERT INTO Students (id, name, age) 
VALUES 
(1, 'Alice', 22), 
(2, 'Bob', 23), 
(3, 'Charlie', 22);

-- 3. Select Query
SELECT name 
FROM Students 
WHERE age = 22;

-- 4. Update Statement
UPDATE Students 
SET name = 'Robert' 
WHERE id = 2;

-- 5. Delete Statement
DELETE FROM Students 
WHERE name = 'Charlie';
