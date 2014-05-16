from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class core2baseTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "core2base"
