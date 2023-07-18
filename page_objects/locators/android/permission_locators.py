from selenium.webdriver.common.by import By

from page_objects.base import Base


class PermissionLocators(Base):
    """Application locators"""
    textTiteView = (By.XPATH, '//android.widget.TextView[@resource-id="titleTextView"]')
    bodyTextView = (By.XPATH, '//android.widget.TextView[@resource-id="bodyTextView"]')
    adjust_button = (By.XPATH, '//android.view.View[@resource-id="adjustButton"]')
    continueButton = (By.XPATH, '//android.view.View[@resource-id="continueButton"]')

    def get_title_text(self): return self.find_elements(self.textTiteView)

    def get_description_text(self): return self.find_elements(self.bodyTextView)

    def get_adjust_button(self): return self.find_elements(self.adjust_button)

    def get_continue_button(self): return self.find_element(self.continueButton)

    """Android native locators"""
    android_switch_widget = (By.ID, 'android:id/switch_widget')
    android_positive_button = (By.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]')
    android_allow_button = (
        By.XPATH, '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]')

    def get_switch(self): return self.find_element(self.android_switch_widget)

    def get_positive_button(self): return self.find_element(self.android_positive_button)

    def get_app_text(self, app_version):
        android_app_textview_content = (By.XPATH, f'//android.widget.TextView[@content-desc="{app_version}"]')
        return self.find_element(android_app_textview_content)

    def get_allow_button(self): return self.find_element(self.android_allow_button)
