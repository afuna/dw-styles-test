from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class fiveamTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "fiveam"
