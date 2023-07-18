from selenium.webdriver.common.by import By

from page_objects.base import Base


class ActivationLocators(Base):
    """Activation screen"""
    textTiteView = (By.XPATH, '//android.widget.TextView[@resource-id="titleTextView"]')
    bodyTextView = (By.XPATH, '//android.widget.TextView[@resource-id="bodyTextView"]')
    tokenEditText = (By.XPATH, '//android.widget.EditText[@resource-id="enterTokenEditText"]')
    activateButton = (By.XPATH, '//android.view.View[@resource-id="activateButton"]')

    def get_logo(self):
        logoImage = (By.XPATH, '//android.view.View[@resource-id="logoImage"]')
        return self.find_element(logoImage)

    def get_title(self): return self.find_element(self.textTiteView)

    def get_description(self): return self.find_element(self.bodyTextView)

    def get_edit_text(self): return self.find_element(self.tokenEditText)

    def get_activate_button(self): return self.find_element(self.activateButton)

    """Activation error - Activation error"""

    def get_error_title(self, title):
        error_title = (By.XPATH, f'//android.widget.TextView[@text="{title}"]')
        return self.find_element(error_title)

    def get_error_desc(self, desc):
        error_desc = (By.XPATH, f'//android.widget.TextView[@text="{desc}"]')
        return self.find_element(error_desc)

    def get_close_button(self):
        close_button = (By.XPATH, '//android.widget.TextView[@text="Close"]')
        return self.find_element(close_button)
