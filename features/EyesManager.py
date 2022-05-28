from applitools.common import MatchLevel
from applitools.selenium import Eyes
from features.browser import Browser
from features.resources.test_config.my_config import APPLITOOLS_API_KEY, APP_NAME


class EyesManager(Browser):
    eyes = Eyes()
    eyes.api_key = APPLITOOLS_API_KEY

    def open_eyes(self, scenario):
        self.eyes.open(self.driver, APP_NAME, test_name=scenario)

    def validate_window(self, scenario, tag=None):
        self.open_eyes(scenario)
        self.eyes.match_level = MatchLevel.CONTENT
        self.eyes.check_window(tag=tag)
        self.close_eyes()

    def validate_full_window(self, scenario, tag=None):
        self.open_eyes(scenario)
        # self.eyes.match_level = MatchLevel.CONTENT
        self.eyes.force_full_page_screenshot = True
        self.eyes.check_window(tag=tag)
        self.close_eyes()

    def validate_region(self, scenario, element, tag=None):
        self.open_eyes(scenario)
        self.eyes.match_level = MatchLevel.LAYOUT
        self.eyes.check_region(element, tag)
        self.close_eyes()

    def validate_region_in_frame(self,scenario, frame_ref, element_tuple, tag=None):
        self.open_eyes(scenario)
        self.eyes.check_region_in_frame(frame_ref, element_tuple, tag)
        self.close_eyes()

    def close_eyes(self):
        self.eyes.close()
