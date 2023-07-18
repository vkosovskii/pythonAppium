from helpers.logger import gen_logger
from page_objects.screen.activation_screen import ActivationScreen
from page_objects.screen.dashboard_screen import DashboardScreen
from page_objects.screen.permission_screen import PermissionScreen
from page_objects.screen.privacy_policy_screen import PrivacyPolicyScreen
from settings import Config

logger = gen_logger("TestScan")
test_data = Config().get_test_data()


class TestScan:

    def test_first_scan(self, driver):
        logger.info("First sacn test")
        policy = PrivacyPolicyScreen(driver)
        activation = ActivationScreen(driver)
        permission = PermissionScreen(driver)
        dashboard = DashboardScreen(driver)

        policy.verify_display()
        policy.click_accept_button()

        activation.verify_display()
        activation.enter_token(test_data['login']['staging'])
        activation.click_activate_button()

        permission.grant_storage_permission()
        permission.grant_background_permission()
        permission.grant_display_over_apps_permission("Business ST")
        permission.grant_usage_data_permission()
        permission.grant_push_notification_permission()
        permission.click_continue_button()

        dashboard.verify_display()
        dashboard.check_last_scan_status("Never")
        dashboard.check_database_status("Preparing…")
        dashboard.click_scan_button()
        dashboard.check_database_status("Updating…")
        dashboard.check_database_status("Updated")
        dashboard.check_scan_is_started()
        dashboard.check_scan_is_finished()
