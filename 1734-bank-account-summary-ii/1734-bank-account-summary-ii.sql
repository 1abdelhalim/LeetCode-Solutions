# Write your MySQL query statement below
Select u.name, sum(t.amount) as balance  
From Users u  
Join Transactions t 
on u.account = t.account 
Group by 1 
Having sum(t.amount) > 10000; 