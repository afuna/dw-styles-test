from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class mobilityTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "mobility"
