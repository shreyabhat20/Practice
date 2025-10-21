--lists out the employee names whose salary is the 3rd highest in the company
SELECT emp_name, salary
FROM employees
WHERE salary = (
    SELECT DISTINCT salary
    FROM employees
    ORDER BY salary DESC
    OFFSET 2 LIMIT 1
);
