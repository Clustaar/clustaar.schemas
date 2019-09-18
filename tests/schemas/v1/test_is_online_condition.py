from clustaar.schemas.v1 import IS_ONLINE_CONDITION
from clustaar.schemas.models import IsOnlineCondition
import pytest


@pytest.fixture
def condition():
    return IsOnlineCondition()


@pytest.fixture
def data():
    return {
        "type": "is_online"
    }


class TestDump(object):
    def test_returns_data(self, condition, data, mapper):
        result = mapper.dump(condition)
        assert data == result


class TestLoad(object):
    def test_returns_a_condition(self, condition, data, mapper):
        condition = mapper.load(data, IS_ONLINE_CONDITION)
        assert isinstance(condition, IsOnlineCondition)
