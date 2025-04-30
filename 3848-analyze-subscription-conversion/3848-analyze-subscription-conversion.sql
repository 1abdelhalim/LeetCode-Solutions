# Write your MySQL query statement below
Select 
distinct t1.user_id,
round((sum(t1.activity_duration) / count(*)), 2) as trial_avg_duration,
round((sum(t2.activity_duration) / count(*)), 2) as paid_avg_duration

From UserActivity t1 
Join UserActivity t2 
On t1.user_id = t2.user_id 
Where t1.activity_type = 'free_trial' and t2.activity_type = 'paid' 
Group by user_id 
