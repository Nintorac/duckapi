select (columns(*)::json)::varchar from {{ ref('analysis') }}
except
select (columns(*)::json)::varchar
from read_json('data/expected_analysis.json')
