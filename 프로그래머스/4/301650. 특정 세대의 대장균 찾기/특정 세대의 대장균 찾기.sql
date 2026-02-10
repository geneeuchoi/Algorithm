-- 코드를 작성해주세요

with fir as (
    select ID
    from ECOLI_DATA
    where PARENT_ID is null
),
second as (
    select e.ID
    from ECOLI_DATA e inner join fir f on e.PARENT_ID = f.ID
)

select e.ID
from ECOLI_DATA e inner join second s on e.PARENT_ID = s.ID
order by e.ID