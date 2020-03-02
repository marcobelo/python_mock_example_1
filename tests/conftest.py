import pytest


@pytest.fixture(name="mock_func", scope="session")
def fixture_mock_func():
    def _mock_func(param1, param2):
        returns = {
            "test_1": {"10": "test_1 with value 10", "20": "test_1 with value 20"},
            "test_2": {"30": "test_2 with value 30", "40": "test_2 with value 40"},
        }

        return returns[param1][param2]

    return _mock_func
