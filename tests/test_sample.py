def test_sample() -> None:
    assert True


def test_sample_with_fixture(sample_fixture: dict) -> None:
    assert sample_fixture["key"] == "value"
