from helpers.logger import gen_logger
from page_objects.locators.android.activation_locators import ActivationLocators

logger = gen_logger("ActivationScreen")


class ActivationScreen(ActivationLocators):

    def verify_display(self):
        logger.info("Verify display")
        self.is_visible(self.get_logo())
        self.is_visible(self.get_title())
        self.is_visible(self.get_description())
        self.is_visible(self.get_edit_text())
        self.is_visible(self.get_activate_button())

    def enter_token(self, token):
        logger.info(f"Enter token {token}")
        self.send_keys(self.get_edit_text(), token)

    def click_activate_button(self):
        logger.info("Click Activate button")
        self.click(self.get_activate_button())

    def verify_error_view(self, title, desc):
        logger.info("Check error screen")
        self.wait_visible(self.get_error_title(title))
        self.is_visible(self.get_error_desc(desc))
        self.is_visible(self.get_close_button())

    def click_close_button(self):
        logger.info("Click Close button")
        self.click(self.get_close_button())
