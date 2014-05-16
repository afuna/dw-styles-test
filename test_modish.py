from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class modishTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "modish"
