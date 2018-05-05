import pytest

@pytest.mark.usefixtures("oneTimeSetup")
class Test_Scenario1():

    def test_step1(self):
        print("Running step 1")
    def test_step2(self):
        print("Running step 2")

