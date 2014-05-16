from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class modularTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "modular"
