-- 코드를 작성해주세요
select e1.ID, e1.GENOTYPE, e2.GENOTYPE as "PARENT_GENOTYPE"
from ECOLI_DATA e1 left join ECOLI_DATA e2 on e1.PARENT_ID = e2.ID
where (e1.GENOTYPE | e2.GENOTYPE) = e1.GENOTYPE
order by e1.ID