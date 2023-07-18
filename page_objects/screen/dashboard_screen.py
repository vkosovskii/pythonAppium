from helpers.logger import gen_logger
from page_objects.locators.android.dashboard_locators import DashboardLocators

logger = gen_logger("DashboardScreen")


class DashboardScreen(DashboardLocators):

    def verify_display(self):
        logger.info("verify display")
        self.is_visible(self.get_logo_component())
        self.is_visible(self.get_help_screen_button())

        self.is_visible(self.get_status_image_component())
        self.is_visible(self.get_status_title())
        self.is_visible(self.get_status_subtitle())

        self.is_visible(self.get_start_scan_button())

        self.is_visible(self.get_security_item_text())
        self.is_visible(self.get_security_item_status())

    def click_help_button(self):
        logger.info("click help button")
        self.click(self.get_help_screen_button())

    def click_scan_button(self):
        logger.info("click scan button")
        self.click(self.get_start_scan_button())

    def wait_until_scan_now_button_is_clickable(self):
        logger.info("wait until scan now button is enabled")
        self.wait_until_enabled(self.get_start_scan_button())

    def check_database_status(self, status):
        logger.info(f"check database status: {status}")
        self.wait_for_text(locator=self.get_info_title_text()[0],
                           text="Database",
                           locator_from_list=True)
        self.wait_for_text(locator=self.get_info_title_status()[0],
                           text=status,
                           locator_from_list=True)

    def check_scan_status(self, status):
        logger.info(f"check scan status: {status}")
        self.wait_for_text(locator=self.get_info_title_text()[1],
                           text="Last scan",
                           locator_from_list=True)
        self.wait_for_text(locator=self.get_info_title_status()[1],
                           text=status,
                           locator_from_list=True)

    def check_last_scan_status(self, status):
        logger.info(f"Check last scan status: {status}")
        self.wait_for_text(self.get_info_title_text()[1], 'Last scan', locator_from_list=True)
        self.wait_for_text(self.get_info_title_status()[1], status, locator_from_list=True)

    def check_rtp_status(self, status):
        logger.info(f"check RTP status: {status}")
        self.wait_for_text(self.get_security_item_text(), "Real-time Protection")
        self.wait_for_text(self.get_security_item_status(), status)

    def check_scan_is_started(self):
        logger.info("check is scan started")
        self.wait_not_visible(self.get_status_image_component())
        self.wait_visible(self.get_circular_progress_indicator())
        self.wait_visible(self.get_percentage_status_indicator())
        self.wait_for_text(self.get_status_title(), "Scan in progress…")
        self.wait_for_text(self.get_status_subtitle(), "Your endpoint is being scanned")
        self.wait_for_text(self.get_start_scan_button(), "Stop scanning")

    def check_scan_is_finished(self):
        logger.info("check is scan finished")
        self.wait_for_text(self.get_percentage_status_indicator(), "100%", 300)
        self.wait_for_text(self.get_start_scan_button(), "Scan now")
        self.wait_for_text(self.get_info_title_status()[1], "Today", True)
        self.is_visible(self.get_status_image_component())
