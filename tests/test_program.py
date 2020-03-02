from unittest import mock
from app.program import start


def test_start_with_function_a_mocked(mock_func):
    mock_patch = "app.program.function_a"
    with mock.patch(mock_patch) as mck:
        mck.side_effect = mock_func

        result = start("test_1", "20")

        assert result == "test_1 with value 20"


def test_start_with_function_a_not_mocked(mock_func):
    result = start("test_1", "20")

    assert result == "name=test_1, value=20"
