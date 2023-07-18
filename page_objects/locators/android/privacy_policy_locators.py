from selenium.webdriver.common.by import By

from page_objects.base import Base


class PrivacyPolicyLocators(Base):
    textTiteView = (By.XPATH, '//android.widget.TextView[@resource-id="titleTextView"]')
    bodyTextView = (By.XPATH, '//android.widget.TextView[@resource-id="bodyTextView"]')
    acceptPolicyButton = (By.XPATH, '//android.view.View[@resource-id="acceptPolicyButton"]')

    def get_logo(self):
        logoImage = (By.XPATH, '//android.view.View[@resource-id="logoImage"]')
        return self.find_element(logoImage)

    def get_title(self): return self.find_element(self.textTiteView)

    def get_description(self): return self.find_element(self.bodyTextView)

    def get_accept_button(self): return self.find_element(self.acceptPolicyButton)


