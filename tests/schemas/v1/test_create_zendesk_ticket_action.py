import pytest

from clustaar.schemas.v1 import CREATE_ZENDESK_TICKET_ACTION
from clustaar.schemas.models import CreateZendeskTicketAction
from lupin.errors import InvalidDocument, InvalidLength
from clustaar.schemas.constants import (
    ZENDESK_TICKET_TYPES,
    ZENDESK_TAG_MAX_LENGTH,
    ZENDESK_TAGS_MAX_COUNT,
    ZENDESK_NAME_MAX_LENGTH,
    ZENDESK_EMAIL_MAX_LENGTH,
    ZENDESK_SUBJECT_MAX_LENGTH,
    ZENDESK_GROUP_ID_MAX_LENGTH,
    ZENDESK_ASSIGNEE_ID_MAX_LENGTH,
    ZENDESK_DESCRIPTION_MAX_LENGTH,
)


@pytest.fixture
def action():
    return CreateZendeskTicketAction(
        name="Je suis un super test",
        email="Tintin@doe.fifi",
        subject="Tester cette action",
        description="Pfff aucune idée",
        group_id="b2" * 12,
        assignee_id="a1" * 12,
        phone_number="0611654852",
        tags=["finished", "fish", "turtle"],
        ticket_type=list(ZENDESK_TICKET_TYPES)[0]
    )


@pytest.fixture
def data():
    return {
        "type": "create_zendesk_ticket_action",
        "name": "Je suis un super test",
        "email": "Tintin@doe.fifi",
        "subject": "Tester cette action",
        "description": "Pfff aucune idée",
        "groupID": "b2" * 12,
        "assigneeID": "a1" * 12,
        "phoneNumber": "0611654852",
        "tags": ["finished", "fish", "turtle"],
        "ticketType": list(ZENDESK_TICKET_TYPES)[0]
    }


def assert_raise_on_length(mapper, data):
    with pytest.raises(InvalidDocument) as errors:
        mapper.validate(data, CREATE_ZENDESK_TICKET_ACTION)

    error = errors.value[0]
    assert isinstance(error, InvalidLength)


class TestDump(object):
    def test_returns_a_dict(self, action, data, mapper):
        result = CREATE_ZENDESK_TICKET_ACTION.dump(action, mapper)
        assert result == data


class TestLoad(object):
    def test_returns_an_action(self, data, mapper):
        action = mapper.load(data, CREATE_ZENDESK_TICKET_ACTION)
        assert isinstance(action, CreateZendeskTicketAction)


class TestValidate(object):
    def test_raise_if_dirty_name(self, mapper, data):
        data["name"] = ""
        assert_raise_on_length(mapper, data)

        data["name"] = "a" * (ZENDESK_NAME_MAX_LENGTH + 1)
        assert_raise_on_length(mapper, data)

    def test_raise_if_dirty_email(self, mapper, data):
        data["email"] = ""
        assert_raise_on_length(mapper, data)

        data["email"] = "a" * (ZENDESK_EMAIL_MAX_LENGTH + 1)
        assert_raise_on_length(mapper, data)

    def test_raise_if_dirty_subject(self, mapper, data):
        data["subject"] = "a" * (ZENDESK_SUBJECT_MAX_LENGTH + 1)
        assert_raise_on_length(mapper, data)

    def test_raise_if_dirty_description(self, mapper, data):
        data["description"] = "a" * (ZENDESK_DESCRIPTION_MAX_LENGTH + 1)
        assert_raise_on_length(mapper, data)

    def test_raise_if_dirty_group_id(self, mapper, data):
        data["groupID"] = "a" * (ZENDESK_GROUP_ID_MAX_LENGTH + 1)
        assert_raise_on_length(mapper, data)

    def test_raise_if_dirty_assignee_id(self, mapper, data):
        data["groupID"] = "a" * (ZENDESK_ASSIGNEE_ID_MAX_LENGTH + 1)
        assert_raise_on_length(mapper, data)

    def test_raise_if_dirty_tags(self, mapper, data):
        data["tags"] = [str(n) for n in range((ZENDESK_TAGS_MAX_COUNT + 1))]
        assert_raise_on_length(mapper, data)

        data["tags"] = ["a" * (ZENDESK_TAG_MAX_LENGTH + 1)]
        assert_raise_on_length(mapper, data)
