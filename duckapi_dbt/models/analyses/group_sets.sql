select
    group_id
    , list(distinct event_value) as group_value_set
from {{ ref('group_event_values') }}
group by group_id
