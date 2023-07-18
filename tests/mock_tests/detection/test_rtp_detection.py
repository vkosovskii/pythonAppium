from helpers.file_manager import android_push_file, android_clear_downloads, android_check_folder_empty
from helpers.logger import gen_logger
from page_objects.Activation_steps import android_activate_local_test
from settings import Config

logger = gen_logger("RTP Detection")
test_data = Config().get_test_data()


class TestRtpDetection:

    def test_file_system(self, driver):
        logger.info("\nRTP Detection - test_file_system")
        android_clear_downloads()

    def test_ransomware_detection(self, driver):
        logger.info("\nRTP Detection - ransomware detection")
        android_clear_downloads()
        android_activate_local_test(driver)
        android_push_file(driver, test_data['files']['Game_Killer'])
        android_check_folder_empty()

    def test_upload_several_threats(self, driver):
        logger.info("\nRTP Detection - ransomware detection")
        android_clear_downloads()
        android_activate_local_test(driver)
        android_push_file(driver, test_data['files']['Game_Killer'])
        android_push_file(driver, test_data['files']['Not_a_virus'])
        android_push_file(driver, test_data['files']['Potential_ransomware'])
        android_push_file(driver, test_data['files']['Ransomware'])
        android_check_folder_empty()
