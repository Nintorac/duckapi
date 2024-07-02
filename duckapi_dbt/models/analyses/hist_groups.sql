select
    group_id
    , count(*) as group_count
from {{ ref('group_event_values') }}
group by group_id
