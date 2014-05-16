from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class corinthianTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "corinthian"
