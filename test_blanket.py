from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class blanketTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "blanket"
