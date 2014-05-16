from layout import LayoutTestCase
from needle.cases import NeedleTestCase

class databaseTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "database"
