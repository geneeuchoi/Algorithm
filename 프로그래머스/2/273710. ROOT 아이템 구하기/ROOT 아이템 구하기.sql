-- 코드를 작성해주세요
select t.ITEM_ID, i.ITEM_NAME
from ITEM_TREE t left join ITEM_INFO i on t.ITEM_ID = i.ITEM_ID
where t.PARENT_ITEM_ID is null
order by t.ITEM_ID