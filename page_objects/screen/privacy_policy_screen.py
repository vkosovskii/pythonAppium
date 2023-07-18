from helpers.logger import gen_logger
from page_objects.locators.android.privacy_policy_locators import PrivacyPolicyLocators

logger = gen_logger("PrivacyPolicyScreen")


class PrivacyPolicyScreen(PrivacyPolicyLocators):

    def verify_display(self):
        logger.info("Verify display")
        self.wait_visible(self.get_logo())
        self.is_visible(self.get_title())
        self.is_visible(self.get_description())
        self.is_visible(self.get_accept_button())

    def click_accept_button(self):
        logger.info("Click accept button")
        self.swipe_down()
        self.swipe_down()
        self.wait_until_enabled(self.get_accept_button())
        self.click(self.get_accept_button())
