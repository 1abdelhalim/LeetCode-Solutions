SELECT d.name as Department, e.name as Employee , e.salary as Salary
FROM Employee e
join Department d
on d.id = e.departmentId
WHERE salary = (
    SELECT MAX(salary)
    FROM Employee
    WHERE departmentId = e.departmentId
);
