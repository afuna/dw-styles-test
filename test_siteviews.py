from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class siteviewsTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "siteviews"
