-- 코드를 작성해주세요
with child as (select ITEM_ID
    from ITEM_INFO
    where RARITY = "RARE"
),
selected as (
    select t.ITEM_ID
    from child c inner join ITEM_TREE t on c.ITEM_ID = t.PARENT_ITEM_ID
)

select s.ITEM_ID, i.ITEM_NAME, i.RARITY
from selected s left join ITEM_INFO i on s.ITEM_ID = i.ITEM_ID
order by s.ITEM_ID desc