from unittest import TestCase

from conversion import convert_to_base_10


class TestConvertToBase10(TestCase):

    def setUp(self):
        b = 7
        x = 314256
        self.y = convert_to_base_10(str(x), b)

    def test_returns_int(self):
        assert isinstance(self.y, int)

    def test_y_result(self):
        assert self.y == 54333
