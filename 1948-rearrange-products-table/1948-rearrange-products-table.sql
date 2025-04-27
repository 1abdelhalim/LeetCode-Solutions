# Write your MySQL query statement below
select product_id, 'store1' as store, store1 as price 
From Products 
Where store1 is not null 


Union all 

select product_id, 'store2' as store, store2 as price 
From Products 
Where store2 is not null 

Union All 

select product_id, 'store3' as store, store3 as price 
From Products 
Where store3 is not null 