import  pytest
@pytest.fixture(scope="module")
def preWork():
    print("I setup module instance")


def test_initialcheck(preWork):
    print("This is first test")


def test_Secondcheck(preSetupWork):
    print("This is Second test")