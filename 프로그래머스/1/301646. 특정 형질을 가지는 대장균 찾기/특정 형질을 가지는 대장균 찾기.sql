-- 코드를 작성해주세요

with n2 as (select *
from ECOLI_DATA
where GENOTYPE & 2 = 0)

select count(*) as "COUNT"
from n2
where GENOTYPE & 1 > 0 or GENOTYPE & 4 > 0 