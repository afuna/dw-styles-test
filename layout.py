from nose.plugins.skip import Skip, SkipTest
from nose.plugins.multiprocess import MultiProcess
import sys

class LayoutTestCase(object):
    engine_class = 'needle.engines.perceptualdiff_engine.Engine'

    ## HELPER METHODS
    def fetch_with_layout(self, layout, layout_type):
        self.driver.get("%s&layout=%s&layout_type=%s" % ('http://www.dream.fu/customize/preview_redirect?as=afuna', layout, layout_type))

    def check_body(self, layout_type, viewport):
        self.fetch_with_layout(self.layout, layout_type)

        if hasattr(self, 'element'):
            element = self.element
        else:
            element = "#canvas"

        self.assertScreenshot(element, "%s-%s-%s" % (self.layout, layout_type, viewport))

    def check_desktop(self, layout_type):
        self.set_viewport_size(width=1024, height=768)
        self.check_body(layout_type, "desktop")

    def check_mobile(self, layout_type):
        self.set_viewport_size(width=360, height=640)
        self.check_body(layout_type, "mobile")

    ## TESTS
    def test_desktop_one_column(self):
        self.check_desktop("one-column")

    def test_desktop_one_column_split(self):
        # raise SkipTest
        self.check_desktop("one-column-split")

    def test_desktop_two_columns_left(self):
        self.check_desktop("two-columns-left")

    def test_desktop_two_columns_right(self):
        # raise SkipTest
        self.check_desktop("two-columns-right")

    def test_desktop_three_columns_sides(self):
        self.check_desktop("three-columns-sides")

    def test_desktop_three_columns_left(self):
        # raise SkipTest
        self.check_desktop("three-columns-left")

    def test_desktop_three_columns_right(self):
        # raise SkipTest
        self.check_desktop("three-columns-right")

    def test_mobile_one_column(self):
        self.check_mobile("one-column")

    def test_mobile_one_column_split(self):
        # raise SkipTest
        self.check_mobile("one-column-split")

    def test_mobile_two_columns_left(self):
        self.check_mobile("two-columns-left")

    def test_mobile_two_columns_right(self):
        # raise SkipTest
        self.check_mobile("two-columns-right")

    def test_mobile_three_columns_sides(self):
        self.check_mobile("three-columns-sides")

    def test_mobile_three_columns_left(self):
        # raise SkipTest
        self.check_mobile("three-columns-left")

    def test_mobile_three_columns_right(self):
        # raise SkipTest
        self.check_mobile("three-columns-right")
