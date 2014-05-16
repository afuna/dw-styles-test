from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class wideopenTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "wideopen"
