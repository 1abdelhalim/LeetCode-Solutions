# Write your MySQL query statement below
Select transaction_date, 
sum(Case when amount % 2 != 0 then amount else 0 end ) as odd_sum,
sum(Case when amount % 2 = 0 then amount else 0 end) as even_sum 
From transactions 
Group by 1
order by transaction_date;