import pytest


@pytest.mark.skip(reason="skip test")
def test_feature_in_development():
    ...


@pytest.mark.skip(reason="skip test")
class TestSuiteSkip:
    def test_feature_in_development_1():
        ...

    def test_feature_in_development_2():
        ...