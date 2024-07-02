.PHONY: test fluff data_build install_dev data_build make_request run_api

mr = curl -s -X POST -H "Content-Type: application/json" \
		-d '[{"group_id": "🦆", "event_value": 13}, {"group_id": "🐇", "event_value": 8}, {"group_id": "🐰", "event_value": 2}, {"group_id": "🐰", "event_value": 5}, {"group_id": "🦆", "event_value": 3}, {"group_id": "🐇", "event_value": 23}, {"group_id": "🐇", "event_value": 1}, {"group_id": "🦆", "event_value": 17}, {"group_id": "🐰", "event_value": 5}]' http://localhost:8000/analyse_data/

test:
	pytest

fluff:
	sqlfluff fix

install_dev:
	poetry install --with dev

data_build:
	dbt build

run_api:
	fastapi dev duckapi/api.py

make_request:
	${mr}

make_request_pretty:
	${mr} | jq
