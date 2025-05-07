# Write your MySQL query statement below
Select t1.product_id as product1_id,
t2.product_id as product2_id, 
p1.category as product1_category, 
p2.category as product2_category, 
Count(distinct t1.user_id) as customer_count
From ProductPurchases t1 
Join ProductPurchases  t2 
on t1.user_id = t2.user_id 
and t1.product_id  < t2.product_id
Left Join ProductInfo p1 
On p1.product_id = t1.product_id
Left Join ProductInfo p2
On p2.product_id = t2.product_id
Group by 1, 2
having count(*) > 2 
Order By customer_count Desc, 1, 2 