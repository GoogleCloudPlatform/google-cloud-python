from unittest.mock import patch

from proto.marshal.marshal import Marshal


def test_marshal_identity():
    m1 = Marshal(name="foo")
    m2 = Marshal(name="foo")
    assert m1 is m2


def test_marshal_different_names():
    m1 = Marshal(name="foo")
    m2 = Marshal(name="bar")
    assert m1 is not m2


def test_marshal_new_race_condition():
    # Test the case where klass is None at line 266,
    # but NOT None at line 271 (another thread created it).

    from unittest.mock import MagicMock

    mock_instances = MagicMock()

    call_count = 0

    def get_side_effect(name, default=None):
        nonlocal call_count
        call_count += 1
        if call_count == 1:
            return None  # First check returns None
        # Simulate another thread having created it
        return "fake_instance"

    mock_instances.get.side_effect = get_side_effect

    with patch.object(Marshal, "_instances", mock_instances):
        instance = Marshal(name="race_test")
        assert instance == "fake_instance"


def test_get_rule_uninitialized_instance():
    class FakeMarshal:
        # No _rules attribute
        pass

    m = Marshal(name="default")

    # Inject FakeMarshal into Marshal._instances safely using patch.dict
    with patch.dict(Marshal._instances, {"fake_uninitialized": FakeMarshal()}):

        class DummyType:
            pass

        # This should not raise AttributeError because of getattr safety
        rule = m.get_rule(DummyType)
        assert rule == m._noop
