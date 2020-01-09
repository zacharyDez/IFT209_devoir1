from unittest import TestCase

from conversion import convert_to_base_10


class TestConvertToBase10(TestCase):

    def setUp(self):
        self.b = 7
        self.x = 314256

    def test_returns_int(self):
        y = convert_to_base_10(self.x, self.b)
        assert isinstance(y, int)

    def test_y_result_x_is_int(self):
        y = convert_to_base_10(self.x, self.b)
        assert y == 54333

    def test_y_result_x_is_str(self):
        y = convert_to_base_10(str(self.x), self.b)
        assert y == 54333
