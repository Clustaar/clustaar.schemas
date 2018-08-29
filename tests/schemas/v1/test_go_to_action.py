import pytest
from clustaar.schemas.v1 import GO_TO_ACTION
from clustaar.schemas.models import StepTarget, GoToAction


@pytest.fixture
def action():
    target = StepTarget(step_id="a1" * 12,
                        name="a step")
    return GoToAction(target=target, extra_session={"aa": 1, "bb": 2})


@pytest.fixture
def data():
    return {
        "type": "go_to_action",
        "target": {
            "type": "step",
            "name": "a step",
            "id": "a1" * 12
        },
        "extraSession": {
            "aa": 1,
            "bb": 2
        }
    }


class TestDump(object):
    def test_returns_a_dict(self, action, data, mapper):
        result = GO_TO_ACTION.dump(action, mapper)
        assert result == data


class TestLoad(object):
    def test_returns_an_action(self, data, mapper):
        action = mapper.load(data, GO_TO_ACTION)
        assert isinstance(action, GoToAction)
        assert action.target.step_id == "a1" * 12
