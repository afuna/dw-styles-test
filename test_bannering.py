from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class banneringTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "bannering"
