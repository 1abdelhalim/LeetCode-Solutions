# Write your MySQL query statement below
Select t1.actor_id, t1.director_id 
From ActorDirector t1 
Join ActorDirector t2 
On t1.actor_id = t2.actor_id
And t1.director_id = t2.director_id 
And t1.timestamp != t2.timestamp
Group by 1, 2 
Having Count(*) > 2  