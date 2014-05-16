from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class motionTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "motion"
