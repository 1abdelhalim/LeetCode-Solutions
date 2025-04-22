# Write your MySQL query statement below
Select player_id, min(event_date) as first_login
From Activity 
Group by 1