-- 코드를 작성해주세요
select d.DEPT_ID as "DEPT_ID",
d.DEPT_NAME_EN as "DEPT_NAME_EN",
round(avg(e.SAL), 0) as "AVG_SAL"
from HR_EMPLOYEES e left join HR_DEPARTMENT d on e.DEPT_ID = d.DEPT_ID
group by d.DEPT_ID, d.DEPT_NAME_EN
order by AVG_SAL desc