from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class trifectaTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "trifecta"
