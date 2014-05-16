from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class patsyTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "patsy"
