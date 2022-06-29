from clustaar.schemas.v1 import SEND_CHOICES_LIST_ACTION
from clustaar.schemas.models import Section, Choice, SendChoicesListAction
import pytest


@pytest.fixture
def section():
    return Section(title="A", choices=[Choice(title="Amelin", image_url="image")])


@pytest.fixture
def action(section):
    return SendChoicesListAction(message="hello", sections=[section])


@pytest.fixture
def data(section):
    return {
        "type": "send_choices_list_action",
        "message": "hello",
        "sections": [
            {
                "type": "section",
                "title": section.title,
                "choices": [{"type": "choice", "title": "Amelin", "imageUrl": "image"}],
            }
        ],
    }


@pytest.fixture
def malicious_data():
    return {
        "type": "send_choices_list_action",
        "message": "<script>void();</script>hello",
        "sections": [
            {
                "type": "section",
                "title": "<script>void();</script>A",
                "choices": [
                    {
                        "type": "choice",
                        "title": "<script>void();</script>Amelin",
                        "imageUrl": "<script>void();</script>image",
                    }
                ],
            }
        ],
    }


class TestDump:
    def test_returns_a_dict(self, action, data, mapper):
        result = SEND_CHOICES_LIST_ACTION.dump(action, mapper)
        assert result == data


class TestLoad:
    def test_returns_an_action(self, data, mapper):
        action = mapper.load(data, SEND_CHOICES_LIST_ACTION)
        assert isinstance(action, SendChoicesListAction)
        assert action.message == "hello"
        section = action.sections[0]
        assert section.title == "A"
        choice = section.choices[0]
        assert choice.title == "Amelin"
        assert choice.image_url == "image"

    def test_returns_an_action_malicious(self, malicious_data, mapper):
        action = mapper.load(malicious_data, SEND_CHOICES_LIST_ACTION)
        assert isinstance(action, SendChoicesListAction)
        assert action.message == "&lt;script&gt;void();&lt;/script&gt;hello"
        section = action.sections[0]
        assert section.title == "&lt;script&gt;void();&lt;/script&gt;A"
        choice = section.choices[0]
        assert choice.title == "&lt;script&gt;void();&lt;/script&gt;Amelin"
        assert choice.image_url == "&lt;script&gt;void();&lt;/script&gt;image"
