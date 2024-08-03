# Write your MySQL query statement below
Select E1.employee_id, E1.name, count(E2.reports_to) as reports_count, round(AVG(E2.age)) as average_age
From Employees as E1 
Join Employees as E2
On E1.employee_id = E2.reports_to
group by 1
Order by 1 

