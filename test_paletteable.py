from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class paletteableTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "paletteable"
