from layout import LayoutTestCase
from needle.cases import NeedleTestCase

from nose.plugins.skip import Skip, SkipTest

class leftyTestCase(LayoutTestCase, NeedleTestCase):

    def setUp(self):
        self.layout = "lefty"

    # lefty doesn't implement 3-column layout type
    def test_desktop_three_columns_sides(self):
        raise SkipTest

    def test_desktop_three_columns_left(self):
        raise SkipTest

    def test_desktop_three_columns_right(self):
        raise SkipTest

    def test_mobile_three_columns_sides(self):
        raise SkipTest

    def test_mobile_three_columns_left(self):
        raise SkipTest

    def test_mobile_three_columns_right(self):
        raise SkipTest
