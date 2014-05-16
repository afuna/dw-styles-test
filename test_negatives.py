from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class negativesTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "negatives"
        self.element = "body"
