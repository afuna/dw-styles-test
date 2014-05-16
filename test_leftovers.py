from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class leftoversTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "leftovers"
