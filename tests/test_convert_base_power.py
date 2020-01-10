import pytest
from unittest import TestCase

from conversion import convert_from_base_10, convert_to_base_10, convert_base_a_to_power


class TestConvertBasePower(TestCase):

    def setUp(self):
        self.x = "100111110001101"
        self.x_10 = convert_to_base_10(self.x, 2)
        self.x_16 = convert_from_base_10(self.x_10, 16)

    def test_assertion_error_if_not_power(self):
        with pytest.raises(Exception) as e:
            convert_base_a_to_power(2, 3)

    def test_base_2_16(self):
        assert self.x_16 == "4F8D"

    def test_base_power_matches_results(self):
        assert self.x_16 == convert_base_a_to_power(self.x, 2, 16)