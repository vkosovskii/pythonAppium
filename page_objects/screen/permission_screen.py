from helpers.logger import gen_logger
from page_objects.locators.android.permission_locators import PermissionLocators

logger = gen_logger("PermissionScreen")


class PermissionScreen(PermissionLocators):

    def click_adjust_button_by_title(self, permission_title):
        """need to rewrite method, try to click button ny index"""
        title_list = self.get_title_text()
        index = next((i for i, item in enumerate(title_list) if item.get_attribute("text") == permission_title), -1)
        self.click(self.get_adjust_button()[0])

    def grant_storage_permission(self):
        logger.info("Grant storage permission")
        self.click_adjust_button_by_title("Storage permission")
        self.click(self.get_switch())
        self.tap_back_button()

    def grant_background_permission(self):
        logger.info("Grant background permission")
        self.click_adjust_button_by_title('Background exclusion required')
        self.click(self.get_positive_button())

    def grant_display_over_apps_permission(self, app_type):
        logger.info("Grant display over apps permission")
        self.click_adjust_button_by_title("Display over other apps")
        self.click(self.get_app_text(app_type))
        self.click(self.get_switch())
        self.tap_back_button()
        self.tap_back_button()

    def grant_usage_data_permission(self):
        logger.info("Grant usage data permission")
        self.click_adjust_button_by_title("Access usage data")
        self.click(self.get_switch())
        self.tap_back_button()

    def grant_push_notification_permission(self):
        logger.info("Grant push notification permission")
        self.click_adjust_button_by_title("Push notification")
        self.click(self.get_allow_button())

    def click_continue_button(self):
        logger.info("Click continue button")
        continue_button = self.get_continue_button()
        self.is_visible(continue_button)
        self.click(continue_button)
