# Write your MySQL query statement below
select p.product_name, s.year, s.price
from Sales as s
join Product as p
on s.Product_id = p.product_id