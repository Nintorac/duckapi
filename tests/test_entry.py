import pytest
from duckapi.api import GroupEventValue
from pydantic_core._pydantic_core import ValidationError

@pytest.fixture
def valid_entry():
    return GroupEventValue(group_id="test_group_id", event_value=1)

def test_entry_init(valid_entry):
    assert valid_entry.group_id == "test_group_id"
    assert valid_entry.event_value == 1

def test_entry_group_id_type():
    with pytest.raises(ValidationError):
        GroupEventValue(group_id=4, event_value=1)  # group_id should be a string

def test_entry_event_value_type():
    with pytest.raises(ValidationError):
        GroupEventValue(group_id="test_group_id", event_value="invalid")  # event_value should be an int

def test_entry_group_id_required():
    with pytest.raises(ValidationError):
        GroupEventValue(event_value=1)  # group_id is required

def test_entry_event_value_required():
    with pytest.raises(ValidationError):
        GroupEventValue(group_id="test_group_id")  # event_value is required
