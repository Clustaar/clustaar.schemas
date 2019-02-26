from clustaar.schemas.v1 import SEND_TEXT_ACTION
from clustaar.schemas.models import SendTextAction
import pytest


@pytest.fixture
def action():
    return SendTextAction(alternatives=["Hi", "Hello"], text="Hello")


@pytest.fixture
def action2():
    return SendTextAction(alternatives=["Hi", "Hello"])


@pytest.fixture
def data():
    return {
        "type": "send_text_action",
        "alternatives": ["Hi", "Hello"],
        "text": "Hello"
    }


@pytest.fixture
def data2():
    return {
        "type": "send_text_action",
        "alternatives": ["Hi", "Hello"]
    }


class TestDump(object):
    def test_returns_a_dict(self, action, data, mapper):
        result = SEND_TEXT_ACTION.dump(action, mapper)
        assert result == data

    def test_does_not_return_null_text(self, action2, data2, mapper):
        result = SEND_TEXT_ACTION.dump(action2, mapper)
        assert result == data2


class TestLoad(object):
    def test_returns_an_action(self, data, mapper):
        action = mapper.load(data, SEND_TEXT_ACTION)
        assert isinstance(action, SendTextAction)
        assert action.alternatives == ["Hi", "Hello"]

    def test_fail_load_text(self, data, mapper):
        action = mapper.load(data, SEND_TEXT_ACTION)
        assert action.text is None
