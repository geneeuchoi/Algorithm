-- 코드를 작성해주세요
with max_c as (
    SELECT 
        ID, 
        PERCENT_RANK() OVER (ORDER BY SIZE_OF_COLONY DESC) AS per
    FROM ECOLI_DATA
)

select ID,
case when per <= 0.25 then "CRITICAL"
when per <= 0.5 then "HIGH"
when per <= 0.75 then "MEDIUM"
else "LOW"
end "COLONY_NAME"
from max_c
order by ID