# Write your MySQL query statement below
select W1.id 
from Weather as W1, Weather as W2
where W1.temperature > W2.temperature and DATEDIFF(w1.recordDate , w2.recordDate) = 1 
