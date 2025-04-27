# Write your MySQL query statement below
select user_id, max(time_stamp) as last_stamp
From Logins 
Where  time_stamp Between '2020-01-01 00:00:00' AND '2020-12-31 23:59:59'
Group by 1 
