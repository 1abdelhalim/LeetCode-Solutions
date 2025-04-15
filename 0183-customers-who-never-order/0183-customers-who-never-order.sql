# Write your MySQL query statement below
Select name as Customers
From Customers c 
Where c.id not in (select customerId from Orders)