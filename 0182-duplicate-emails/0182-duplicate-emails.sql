# Write your MySQL query statement below
select email as Email
From Person 
Group by email  
Having count(email) >  1  
