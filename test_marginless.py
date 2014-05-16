from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class marginlessTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "marginless"
