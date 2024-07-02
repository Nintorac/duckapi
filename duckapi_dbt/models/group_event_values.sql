select
    group_id
    , event_value
from {{ ref('example_group_event_values') }}
