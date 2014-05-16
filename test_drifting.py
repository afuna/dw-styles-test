from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class driftingTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "drifting"
