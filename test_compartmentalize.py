from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class compartmentalizeTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "compartmentalize"
