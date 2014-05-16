from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class easyreadTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "easyread"
