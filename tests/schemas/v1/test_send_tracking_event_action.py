from clustaar.schemas.v1 import SEND_TRACKING_EVENT_ACTION
from clustaar.schemas.models import SendTrackingEventAction
import pytest


@pytest.fixture
def action():
    return SendTrackingEventAction(payload={})


@pytest.fixture
def data():
    return {"type": "send_tracking_event_action", "payload": {}}


class TestDump:
    def test_returns_a_dict(self, action, data, mapper):
        result = SEND_TRACKING_EVENT_ACTION.dump(action, mapper)

        assert result == data


class TestLoad:
    def test_returns_an_action(self, data, mapper):
        action = mapper.load(data, SEND_TRACKING_EVENT_ACTION)
        assert isinstance(action, SendTrackingEventAction)
        assert action.payload == {}
