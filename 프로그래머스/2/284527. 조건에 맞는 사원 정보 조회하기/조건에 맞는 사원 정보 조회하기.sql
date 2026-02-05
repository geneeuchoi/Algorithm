-- 코드를 작성해주세요
select g.SCORE, e.EMP_NO, e.EMP_NAME, e.POSITION, e.EMAIL
from HR_EMPLOYEES e left join (select EMP_NO, sum(SCORE) as score
from HR_GRADE
group by EMP_NO) g on e.EMP_NO = g.EMP_NO
order by g.SCORE desc
limit 1