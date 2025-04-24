# Write your MySQL query statement below
Select u.name, ifnull(sum(r.distance), 0) as travelled_distance 
From Users u 
LEft join Rides r 
On u.id = r.user_id 
Group by u.id
Order by 2 desc, 1 
