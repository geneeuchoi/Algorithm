-- 코드를 작성해주세요

with max_size as (select max(SIZE_OF_COLONY) as max_size,
year(DIFFERENTIATION_DATE) as year
from ECOLI_DATA
group by year(DIFFERENTIATION_DATE))

select m.year as "YEAR",
(m.max_size - d.SIZE_OF_COLONY) as "YEAR_DEV",
d.id as "ID"
from ECOLI_DATA d left join max_size m on year(d.DIFFERENTIATION_DATE) = m.year
order by YEAR, YEAR_DEV