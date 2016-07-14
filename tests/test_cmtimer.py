from cmtimer import Timer
from time import sleep


class TimerTests:
    def test_context(self):
        with Timer() as time:
            sleep(.37)
        assert abs(float(time) - .37) < .1

    def test_string(self):
        with Timer() as time:
            sleep(.37)
        assert str(time) == str(float(time))
        assert '{time:.2f}'.format(time=time) == str(round(float(time), 2))

    def test_float(self):
        with Timer() as time:
            sleep(.37)
        assert abs(time - .37) < .1
        assert abs(.37 - time) < .1
