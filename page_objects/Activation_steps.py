from helpers.logger import gen_logger
from helpers.moks import set_mock_config
from page_objects.screen.activation_screen import ActivationScreen
from page_objects.screen.dashboard_screen import DashboardScreen
from page_objects.screen.permission_screen import PermissionScreen
from page_objects.screen.privacy_policy_screen import PrivacyPolicyScreen
from settings import Config

logger = gen_logger("RTP Detection")
test_data = Config().get_test_data()


def android_activate_local_test(driver):
    logger.info("RTP Detection - ransomware detection")
    policy = PrivacyPolicyScreen(driver)
    activation = ActivationScreen(driver)
    permission = PermissionScreen(driver)
    dashboard = DashboardScreen(driver)

    set_mock_config(test_data['mocks']['default'])

    policy.verify_display()
    policy.click_accept_button()

    activation.verify_display()
    activation.enter_token(test_data['login']['staging'])
    activation.click_activate_button()

    permission.grant_storage_permission()
    permission.grant_background_permission()
    permission.grant_display_over_apps_permission(test_data['strings']['appLT'])
    permission.grant_usage_data_permission()
    permission.click_continue_button()

    dashboard.verify_display()
    dashboard.check_scan_status("Never")
    dashboard.check_database_status("Preparing…")
    dashboard.wait_until_scan_now_button_is_clickable()
    dashboard.check_database_status("Updated")

