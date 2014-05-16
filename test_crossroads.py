from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class crossroadsTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "crossroads"
