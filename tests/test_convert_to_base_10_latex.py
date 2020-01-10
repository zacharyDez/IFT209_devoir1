from unittest import TestCase

from conversion import convert_to_base_10_latex


class TestConvertToBase10Latex(TestCase):

    def setUp(self):
        self.b = 7
        self.x = 314256
        self.latex = convert_to_base_10_latex(self.x, self.b)

    def test_returns_str(self):
        assert isinstance(self.latex, str)

    def test_number_of_times_sym_matches_number(self):
        num_times = len(self.latex.split('\\times'))
        # 3 times in initial message
        assert num_times == len(str(self.x))+3

    def test_num_parenthesis_matches(self):
        assert len([l for l in self.latex if l == '(']) == len([l for l in self.latex if l == ')'])
