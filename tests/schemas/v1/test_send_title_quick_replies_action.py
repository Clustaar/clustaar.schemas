from clustaar.schemas.v1 import SEND_TITLE_QUICK_REPLIES_ACTION
from clustaar.schemas.models import TitleQuickReply, SendTitleQuickRepliesAction
import pytest


@pytest.fixture
def quick_reply(go_to_action):
    return TitleQuickReply(title="Ok")


@pytest.fixture
def action(quick_reply):
    return SendTitleQuickRepliesAction(message="Ok?", buttons=[quick_reply])


@pytest.fixture
def data():
    return {
        "type": "send_title_quick_replies_action",
        "message": "Ok?",
        "buttons": [
            {
                "type": "title_quick_reply",
                "title": "Ok",
            }
        ],
    }


@pytest.fixture
def malicious_data():
    return {
        "type": "send_title_quick_replies_action",
        "message": "<script>void();</script>Ok?",
        "buttons": [
            {
                "type": "title_quick_reply",
                "title": "<script>void();</script>Ok",
            }
        ],
    }


class TestDump(object):
    def test_returns_a_dict(self, action, data, mapper):
        result = SEND_TITLE_QUICK_REPLIES_ACTION.dump(action, mapper)
        assert result == data


class TestLoad(object):
    def test_returns_an_action(self, data, mapper):
        action = mapper.load(data, SEND_TITLE_QUICK_REPLIES_ACTION)
        assert isinstance(action, SendTitleQuickRepliesAction)
        assert action.message == "Ok?"
        quick_reply = action.buttons[0]
        assert quick_reply.title == "Ok"

    def test_returns_an_action_malicious(self, malicious_data, mapper):
        action = mapper.load(malicious_data, SEND_TITLE_QUICK_REPLIES_ACTION)
        assert isinstance(action, SendTitleQuickRepliesAction)
        assert action.message == "&lt;script&gt;void();&lt;/script&gt;Ok?"
        quick_reply = action.buttons[0]
        assert quick_reply.title == "&lt;script&gt;void();&lt;/script&gt;Ok"

