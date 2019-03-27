import pytest

from clustaar.schemas.v1 import SEND_USER_INPUT_ACTION
from clustaar.schemas.models import SendUserInputAction
from clustaar.schemas.constants import (
    SEND_USER_INPUT_TEXT_MAX_LENGTH,
    STORE_SESSION_VALUE_ACTION_KEY_MAX_LENGTH
)
from lupin.errors import InvalidDocument, InvalidLength, InvalidIn, InvalidMatch


@pytest.fixture
def action():
    return SendUserInputAction(
        text="Hello",
        kind="email",
        required=False,
        key="foo bar"
    )


@pytest.fixture
def data():
    return {
        "type": "send_user_input_action",
        "text": "Hello",
        "kind": 'email',
        "required": False,
        "key": 'foo bar'
    }


def assert_raise_on_length(mapper, data):
    with pytest.raises(InvalidDocument) as errors:
        mapper.validate(data, SEND_USER_INPUT_ACTION)

    error = errors.value[0]
    assert isinstance(error, InvalidLength)


def assert_raise_on_in(mapper, data):
    with pytest.raises(InvalidDocument) as errors:
        mapper.validate(data, SEND_USER_INPUT_ACTION)

    error = errors.value[0]
    assert isinstance(error, InvalidIn)


def assert_raise_on_match(mapper, data):
    with pytest.raises(InvalidDocument) as errors:
        mapper.validate(data, SEND_USER_INPUT_ACTION)

    error = errors.value[0]
    assert isinstance(error, InvalidMatch)


class TestDump(object):
    def test_returns_a_dict(self, action, data, mapper):
        result = SEND_USER_INPUT_ACTION.dump(action, mapper)
        assert result == data


class TestLoad(object):
    def test_returns_an_action(self, data, mapper):
        action = mapper.load(data, SEND_USER_INPUT_ACTION)
        assert isinstance(action, SendUserInputAction)


class TestValidate(object):
    def test_raise_if_text_is_too_long(self, mapper, data):
        data["text"] = "a" * (SEND_USER_INPUT_TEXT_MAX_LENGTH + 1)
        assert_raise_on_length(mapper, data)

    def test_raise_if_text_is_empty(self, mapper, data):
        data["text"] = ""
        assert_raise_on_length(mapper, data)

    def test_raise_if_kind_is_not_defined(self, mapper, data):
        data["kind"] = "unknown"
        assert_raise_on_in(mapper, data)

    def test_raise_if_key_is_too_long(self, mapper, data):
        data["key"] = "a" * (STORE_SESSION_VALUE_ACTION_KEY_MAX_LENGTH + 1)
        assert_raise_on_length(mapper, data)

    def test_raise_if_key_is_empty(self, mapper, data):
        data["key"] = ""
        assert_raise_on_length(mapper, data)

    def test_raise_if_key_does_not_match(self, mapper, data):
        data["key"] = "@foo"
        assert_raise_on_match(mapper, data)
