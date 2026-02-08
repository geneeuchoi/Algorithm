-- 코드를 작성해주세요


select i.ITEM_ID, i.ITEM_NAME, i.RARITY
from ITEM_INFO i left join ITEM_TREE t on i.ITEM_ID = t.ITEM_ID
WHERE i.ITEM_ID NOT IN (
    SELECT t.PARENT_ITEM_ID 
    FROM ITEM_TREE t 
    WHERE t.PARENT_ITEM_ID IS NOT NULL
)
order by i.ITEM_ID desc
