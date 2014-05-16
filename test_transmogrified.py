from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class transmogrifiedTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "transmogrified"
        self.element = "#container"