select
    group_id
    , event_value
    , count(*) as group_event_value_count
from {{ ref('group_event_values') }}
group by group_id, event_value
