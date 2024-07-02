select
    (
        select list(group_sums) from {{ ref('group_sums') }}
    ) as group_sums
    , (
        select list(group_sets) from {{ ref('group_sets') }}
    ) as group_sets
    , (
        select list(group_event_value_histogram)
        from {{ ref('group_event_value_histogram') }}
    ) as group_event_value_histogram
    , (
        select list(group_histogram) from {{ ref('group_histogram') }}
    ) as group_histogram
    , (
        select list(hist_event_values) from {{ ref('hist_event_values') }}
    ) as hist_event_values
    , (
        select list(hist_group_event_values)
        from {{ ref('hist_group_event_values') }}
    ) as hist_group_event_values
    , (
        select list(hist_groups) from {{ ref('hist_groups') }}
    ) as hist_groups
-- Note: No from in this query.
-- Instead each column is a list of that tables rows.
