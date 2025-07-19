import pytest
@pytest.fixture(scope="module")
def preWork():
    print("I setup module instance")
    return "fail"

@pytest.fixture(scope="function")
def secondWork():
    print("I setup secondWork function instance")
    yield
    print("Tear down validation")


@pytest.mark.smoke
def test_Initialcheck(preWork,secondWork):
    print("This is first test")
    assert preWork == 'fail'

@pytest.mark.skip
def test_Secondcheck(preSetupWork,secondWork):
    print("This is Second test")

@pytest.mark.smoke
def test_Thirdcheck(preSetupWork,secondWork):
    print("This is Third test")