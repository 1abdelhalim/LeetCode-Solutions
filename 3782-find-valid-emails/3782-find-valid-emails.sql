# Write your MySQL query statement below
Select user_id, email 
From Users 
Where email REGEXP '^[a-zA-Z0-9_]+@[a-zA-Z]+\\.com$'

