# Write your MySQL query statement below
Select u.user_id as buyer_id, u.join_date, 
COUNT(CASE WHEN o.order_date BETWEEN '2019-01-01' AND '2019-12-31' THEN 1 END) AS orders_in_2019
From Users u 
LEFT Join Orders o 
On u.user_id = o.buyer_id 
Group by 1 ,2 