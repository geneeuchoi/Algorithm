-- 코드를 작성해주세요

with child as (
    select PARENT_ID, count(PARENT_ID) as "CHILD_COUNT"
    from ECOLI_DATA
    where PARENT_ID is not null
    group by PARENT_ID
)

select d.ID, ifnull(c.CHILD_COUNT, 0) as "CHILD_COUNT"
from ECOLI_DATA d left join child c on d.ID = c.PARENT_ID