from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class abstractiaTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "abstractia"
