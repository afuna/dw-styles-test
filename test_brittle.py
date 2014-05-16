from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class brittleTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "brittle"
