--to find all departments where total salary expenditure is over 500000 and is having more than 10 employees. The result should contain department name and total salary of it
SELECT 
    d.dept_name,
    SUM(e.salary) AS total_salary
FROM 
    employees e
JOIN 
    departments d 
ON 
    e.dept_id = d.dept_id
GROUP BY 
    d.dept_name
HAVING 
    SUM(e.salary) > 500000
    AND COUNT(e.emp_id) > 10;
