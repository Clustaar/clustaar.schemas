from clustaar.schemas.v1 import JUMP_TO_ACTION
from clustaar.schemas.models import FlowConnection, IsSetCondition, MessageGetter, StepTarget,\
    ConnectionPredicate, JumpToAction, IsNotSetCondition, StoryTarget
import pytest


@pytest.fixture
def data():
    return {
        "type": "jump_to_action",
        "connections": [
            {
                "type": "flow_connection",
                "target": {
                    "id": "a2" * 12,
                    "type": "story",
                    "name": "a story"
                },
                "predicates": [
                    {
                        "type": "connection_predicate",
                        "condition": {
                            "type": "is_not_set"
                        },
                        "valueGetter": {
                            "type": "message"
                        }
                    }
                ]
            }
        ],
        "defaultConnection": {
            "type": "flow_connection",
            "target": {
                "id": "a1" * 12,
                "type": "step",
                "name": "a step"
            },
            "predicates": [
                {
                    "type": "connection_predicate",
                    "condition": {
                        "type": "is_set"
                    },
                    "valueGetter": {
                        "type": "message"
                    }
                }
            ]
        }
    }


@pytest.fixture
def action():
    story_connection = FlowConnection(
        predicates=[
            ConnectionPredicate(
                condition=IsNotSetCondition(),
                value_getter=MessageGetter()
            )
        ],
        target=StoryTarget(story_id="a2" * 12, name="a story")
    )
    step_connection = FlowConnection(
        predicates=[
            ConnectionPredicate(
                condition=IsSetCondition(),
                value_getter=MessageGetter()
            )
        ],
        target=StepTarget(step_id="a1" * 12, name="a step")
    )
    return JumpToAction(default_connection=step_connection,
                        connections=[story_connection])


class TestLoad(object):
    def test_returns_an_action(self, data, mapper):
        result = mapper.load(data, JUMP_TO_ACTION)
        assert isinstance(result, JumpToAction)
        assert len(result.connections) == 1

        assert isinstance(result.connections[0], FlowConnection)
        target = result.connections[0].target
        assert isinstance(target, StoryTarget)
        assert target.story_id == "a2" * 12
        predicate = result.connections[0].predicates[0]
        assert isinstance(predicate, ConnectionPredicate)
        assert isinstance(predicate.condition, IsNotSetCondition)
        assert isinstance(predicate.value_getter, MessageGetter)

        assert isinstance(result.default_connection, FlowConnection)
        target = result.default_connection.target
        assert isinstance(target, StepTarget)
        assert target.step_id == "a1" * 12
        predicate = result.default_connection.predicates[0]
        assert isinstance(predicate, ConnectionPredicate)
        assert isinstance(predicate.condition, IsSetCondition)
        assert isinstance(predicate.value_getter, MessageGetter)


class TestDump(object):
    def test_returns_a_dict(self, data, action, mapper):
        result = mapper.dump(action, JUMP_TO_ACTION)
        assert result == data
