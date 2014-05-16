from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class crispedTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "crisped"
