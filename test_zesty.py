from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class zestyTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "zesty"
        self.element = "body"
