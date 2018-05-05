import pytest
from Include.SwapanLib.ProgramTobeTested import ProgramTobeTested

@pytest.mark.usefixtures("SetUpOneTimeClassFixture")
class Test_ClassLvlFixture():
    # Be careful the class name should be started by 'Test' not 'test', then no test under the class be found by pytest
    @pytest.mark.run(order=3)
    def test_Steps3(self):
        self.result=30
        assert self.result == 30
        print("Running 3rd steps of the test2")

    @pytest.mark.run(order=2)
    def test_Steps1(self):
        ProgramObject=ProgramTobeTested(20)
        # The above way to create object is not a good proctive in testin framework
        result=ProgramObject.sum(5,10)
        assert result == 37
        print("Running first steps of the test2")

    @pytest.mark.run(order=1)
    def test_Steps2(self):
        print("Running 2nd steps of the test2")
