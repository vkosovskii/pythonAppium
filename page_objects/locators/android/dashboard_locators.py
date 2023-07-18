from selenium.webdriver.common.by import By

from page_objects.base import Base


class DashboardLocators(Base):
    database_circle_progress_bar = (By.XPATH, '//android.widget.ProgressBar[@resource-id="circularProgressIndicator"]')

    def get_logo_component(self):
        logo_component = (By.XPATH, '//android.view.View[@resource-id="logoComponent"]')
        return self.find_element(logo_component)

    def get_help_screen_button(self):
        help_screen_button = (By.XPATH, '//android.widget.Button[@resource-id="helpScreenButton"]')
        return self.find_element(help_screen_button)

    def get_status_image_component(self):
        status_image_component = (By.XPATH, '//android.view.View[@resource-id="statusImageComponent"]')
        return self.find_element(status_image_component)

    def get_circular_progress_indicator(self):
        circular_progress_indicator = (
        By.XPATH, '//android.widget.ProgressBar[@resource-id="circularProgressIndicator"]')
        return self.find_element(circular_progress_indicator)

    def get_percentage_status_indicator(self):
        percentage_status_indicator = (By.XPATH, '//android.widget.TextView[@resource-id="textView"]')
        return self.find_element(percentage_status_indicator)

    def get_status_title(self):
        status_title = (By.XPATH, '//android.view.View[@resource-id="statusTitleComponent"]')
        return self.find_element(status_title)

    def get_status_subtitle(self):
        status_subtitle = (By.XPATH, '//android.widget.TextView[@resource-id="statusSubtitleComponent"]')
        return self.find_element(status_subtitle)

    def get_title_component(self):
        title_component = (By.XPATH, '//android.widget.TextView[@resource-id="titleComponent"]')
        return self.find_elements(title_component)

    def get_start_scan_button(self):
        start_scan_button = (By.XPATH, '//android.view.View[@resource-id="startScanButton"]')
        return self.find_element(start_scan_button)

    def get_info_title_text(self):
        info_title_text = (By.XPATH, '//android.widget.TextView[@resource-id="scannerStatusText"]')
        return self.find_elements(info_title_text)

    def get_info_title_status(self):
        info_status_text = (By.XPATH, '//android.widget.TextView[@resource-id="clickableText"]')
        return self.find_elements(info_status_text)

    def get_security_item_text(self):
        security_item_text = (By.XPATH, '//android.widget.TextView[@resource-id="securityItemComponentText"]')
        return self.find_element(security_item_text)

    def get_security_item_status(self):
        security_item_status = (By.XPATH, '//android.view.View[@resource-id="securityItemComponentStatus"]')
        return self.find_element(security_item_status)
