from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class sundaymorningTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "sundaymorning"
        self.element = "#container"
