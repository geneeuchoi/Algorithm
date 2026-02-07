-- 코드를 작성해주세요
with j as (select g.EMP_NO, 
e.EMP_NAME,
CASE WHEN avg(g.SCORE) >= 96 THEN "S"
     WHEN avg(g.SCORE) >= 90 THEN "A"
     WHEN avg(g.SCORE) >= 80 THEN "B"
     ELSE "C"
end "GRADE",
e.SAL
from HR_GRADE g left join HR_EMPLOYEES e on g.EMP_NO = e.EMP_NO
group by g.EMP_NO)

select EMP_NO,
EMP_NAME,
GRADE,
case when j.GRADE = "S" then j.SAL * 0.2
when j.GRADE = "A" then j.SAL * 0.15
when j.GRADE = "B" then j.SAL * 0.1
else 0
end "BONUS"
from j
order by EMP_NO