# Write your MySQL query statement below
Select stock_name,
       sum(Case
           When operation ="Sell" Then price
           When operation = "Buy" Then -price
           ELse 0 end) 
           as capital_gain_loss
From Stocks 
Group by 1 
