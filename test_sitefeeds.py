from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class sitefeedsTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "sitefeeds"
