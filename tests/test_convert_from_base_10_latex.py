from unittest import TestCase

from conversion import convert_from_base_10_latex


class TestConvertToBase10Latex(TestCase):

    def setUp(self):
        self.b = 7
        self.x = 314256
        self.latex = convert_from_base_10_latex(self.x, self.b)

    def test_msg_not_empty(self):
        assert self.latex

    def test_returns_str(self):
        assert isinstance(self.latex, str)

    def test_num_parenthesis_matches(self):
        assert len([l for l in self.latex if l == '(']) == len([l for l in self.latex if l == ')'])
