from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class tectonicTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "tectonic"
