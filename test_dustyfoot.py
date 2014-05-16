from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class dustyfootTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "dustyfoot"
