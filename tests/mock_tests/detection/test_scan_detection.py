from helpers.file_manager import android_push_file, android_clear_downloads, android_check_folder_empty
from helpers.logger import gen_logger
from page_objects.Activation_steps import android_activate_local_test
from page_objects.screen.dashboard_screen import DashboardScreen
from settings import Config

logger = gen_logger("RTP Detection")
test_data = Config().get_test_data()


class TestScanDetection:

    def test_first_scan(self, driver):
        logger.info("\nRTP Detection - ransomware detection")
        dashboard = DashboardScreen(driver)
        android_activate_local_test(driver)
        dashboard.click_scan_button()
        dashboard.check_scan_is_started()
        dashboard.check_scan_is_finished()

    def test_ransomware_scan_detection(self, driver):
        logger.info("\nRTP Detection - ransomware detection")
        android_clear_downloads()
        android_activate_local_test(driver)
        android_push_file(driver, test_data['files']['Game_Killer'])
        android_check_folder_empty()

    def test_scan_detect_multiple(self, driver):
        logger.info("\nRTP Detection - ransomware detection")
        android_clear_downloads()
        android_push_file(driver, test_data['files']['Game_Killer'])
        android_push_file(driver, test_data['files']['Not_a_virus'])
        android_push_file(driver, test_data['files']['Potential_ransomware'])
        android_push_file(driver, test_data['files']['Ransomware'])
        android_activate_local_test(driver)
        android_check_folder_empty()
