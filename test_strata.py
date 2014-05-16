from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class strataTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "strata"
