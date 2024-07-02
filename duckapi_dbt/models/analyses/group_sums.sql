select
    group_id
    , sum(event_value) as value_sum
from {{ ref('group_event_values') }}
group by group_id
