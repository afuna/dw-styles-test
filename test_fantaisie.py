from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class fantaisieTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "fantaisie"
