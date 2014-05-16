from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class basesTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "bases"

        # doesn't work for one-column. oh well
        self.element = "body"
