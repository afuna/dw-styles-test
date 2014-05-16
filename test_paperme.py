from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class papermeTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "paperme"
