import json
from pathlib import Path
import pytest
from fastapi.testclient import TestClient
from duckapi.api import GroupEventValue, app, entries_adapter

client = TestClient(app)
data_dir = Path(__file__).parents[1] / 'data'


def test_create_entries():
    entries = [
        GroupEventValue(group_id="group1", event_value=1),
        GroupEventValue(group_id="group2", event_value=2),
    ]
    # raise ValueError(entries_adapter.dump_python(entries)[0])
    response = client.post(
        "/analyse_data/",
        headers={"Content-Type": "application/json"},
        data=entries_adapter.dump_json(entries))

    assert response.status_code == 200
    # bad test
    assert response.json()[0].keys() == json.loads((data_dir / 'expected_analysis.json').read_text())[0].keys()

def test_create_entries_invalid_json():
    response = client.post("/analyse_data/", json="not a list")
    assert response.status_code == 422

def test_create_entries_empty_list():
    response = client.post("/analyse_data/", json=[])
    assert response.status_code == 200
    assert response.json() == []

def test_create_entries_invalid_entry():
    entries = [
        GroupEventValue(group_id="group1", event_value=1).model_dump(),
        {"not": "a valid Entry object"},
    ]
    response = client.post("/analyse_data/", json=entries)
    assert response.status_code == 422
