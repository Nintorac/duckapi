select
    event_value
    , count(*) as event_value_count
from {{ ref('group_event_values') }}
group by event_value
