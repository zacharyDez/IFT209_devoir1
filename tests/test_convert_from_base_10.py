from unittest import TestCase

from conversion import convert_from_base_10


class TestConvertFromBase10(TestCase):

    def setUp(self):
        b = 7
        x = 314256
        self.y = convert_from_base_10(x, b)

    def test_returns_str(self):
        assert isinstance(self.y, str)

    def test_y_result(self):
        assert int(self.y) == 2446125

    def test_base_10_to_3(self):
        assert convert_from_base_10(4820, 3) == "20121112"
