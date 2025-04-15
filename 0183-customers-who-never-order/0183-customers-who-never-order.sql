# Write your MySQL query statement below
Select name as Customers
From Customers c 
left join Orders o 
on c.id = o.customerId
Where o.id is null 