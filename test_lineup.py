from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class lineupTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "lineup"
