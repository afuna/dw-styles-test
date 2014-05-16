from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class headsupTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "headsup"
