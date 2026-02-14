-- 코드를 작성해주세요
select ID, EMAIL, FIRST_NAME, LAST_NAME
from DEVELOPERS
where SKILL_CODE & (
    select SUM(CODE)
    from SKILLCODES c
    where c.CATEGORY="Front End"
) > 0
order by ID