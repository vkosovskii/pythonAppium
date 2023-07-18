from helpers.logger import gen_logger
from helpers.moks import set_mock_config, send_push
from page_objects.screen.activation_screen import ActivationScreen
from page_objects.screen.dashboard_screen import DashboardScreen
from page_objects.screen.permission_screen import PermissionScreen
from page_objects.screen.privacy_policy_screen import PrivacyPolicyScreen
from settings import Config

logger = gen_logger("Activation suite")
test_data = Config().get_test_data()


class TestActivationErrors:

    def test_empty_name_error(self, driver):
        logger.info("Activation - empty name test")
        policy = PrivacyPolicyScreen(driver)
        activation = ActivationScreen(driver)

        set_mock_config(test_data['mocks']['emptyName'])

        policy.verify_display()
        policy.click_accept_button()

        activation.verify_display()
        activation.enter_token(test_data['login']['staging'])
        activation.click_activate_button()
        activation.verify_error_view(test_data['strings']['wrong'], test_data['strings']['contact'])
        activation.click_close_button()

    def test_empty_uuid_error(self, driver):
        logger.info("Activation - empty UUID test")
        policy = PrivacyPolicyScreen(driver)
        activation = ActivationScreen(driver)

        set_mock_config(test_data['mocks']['emptyUUID'])

        policy.verify_display()
        policy.click_accept_button()

        activation.verify_display()
        activation.enter_token(test_data['login']['staging'])
        activation.click_activate_button()
        activation.verify_error_view(test_data['strings']['wrong'], test_data['strings']['contact'])
        activation.click_close_button()

    def test_empty_token_error(self, driver):
        logger.info("Activation - empty token test")
        policy = PrivacyPolicyScreen(driver)
        activation = ActivationScreen(driver)

        set_mock_config(test_data['mocks']['emptyToken'])

        policy.verify_display()
        policy.click_accept_button()

        activation.verify_display()
        activation.enter_token(test_data['login']['staging'])
        activation.click_activate_button()
        activation.verify_error_view(test_data['strings']['wrong'], test_data['strings']['contact'])
        activation.click_close_button()

    def test_server_error(self, driver):
        logger.info("Activation - internal server error test")
        policy = PrivacyPolicyScreen(driver)
        activation = ActivationScreen(driver)

        set_mock_config(test_data['mocks']['internalServerError'])

        policy.verify_display()
        policy.click_accept_button()

        activation.verify_display()
        activation.enter_token(test_data['login']['staging'])
        activation.click_activate_button()
        activation.verify_error_view(test_data['strings']['wrong'], test_data['strings']['contact'])
        activation.click_close_button()

    def test_no_account_exception(self, driver):
        logger.info("Activation - no such account exception test")
        policy = PrivacyPolicyScreen(driver)
        activation = ActivationScreen(driver)

        set_mock_config(test_data['mocks']['noSuchAccountException'])

        policy.verify_display()
        policy.click_accept_button()

        activation.verify_display()
        activation.enter_token(test_data['login']['staging'])
        activation.click_activate_button()
        activation.verify_error_view(test_data['strings']['activationError'], test_data['strings']['anError'])
        activation.click_close_button()

    def test_deactivate_app(self, driver):
        logger.info('Deactivate application test')
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
        permission.grant_display_over_apps_permission("Business LT")
        permission.grant_usage_data_permission()
        permission.click_continue_button()

        dashboard.verify_display()

        set_mock_config(test_data['mocks']['deactivateApp'])
        send_push()
        policy.verify_display()

    def test_auth_and_refresh_machine_token_expired(self, driver):
        logger.info('Deactivate application test')
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
        permission.grant_display_over_apps_permission("Business LT")
        permission.grant_usage_data_permission()
        permission.click_continue_button()

        dashboard.verify_display()

        set_mock_config(test_data['mocks']['AuthTokenExpired'])
        send_push()
        dashboard.verify_display()

        set_mock_config(test_data['mocks']['RefreshTokenExpired'])
        send_push()
        policy.verify_display()
