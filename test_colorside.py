from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class colorsideTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "colorside"
