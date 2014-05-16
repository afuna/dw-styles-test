from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class skittlishdreamsTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "skittlishdreams"
        self.element = "#container"
