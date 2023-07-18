import os
from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

from helpers.logger import gen_logger

logger = gen_logger("Base actions")


class Base:
    global_timeout = 100
    wait_timeout = 20

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self._find_element(locator)

    def find_elements(self, locator):
        return self._find_element(locator, return_multiple_elements=True)

    # get elements
    def _find_element(self, locator, return_multiple_elements=False, retried=False):
        """
        Returns element or elements.

        This will take either a tuple or a list of tuples.
        :param locator:
        :param return_multiple_elements:
        :return:
        """
        try:
            if type(locator) == tuple:
                if return_multiple_elements is False:
                    return self.get_element_by_type(method=locator[0], value=locator[1])
                else:
                    return self.get_elements_by_type(
                        method=locator[0], value=locator[1]
                    )
            elif type(locator) == list:
                for l in locator:
                    try:
                        if return_multiple_elements is False:
                            return self.get_element_by_type(method=l[0], value=l[1])
                        else:
                            return self.get_elements_by_type(method=l[0], value=l[1])
                    except NoSuchElementException:
                        pass
                raise NoSuchElementException
            else:
                raise Exception('Invalid locator type')
        except TypeError:
            if retried is False:
                self._find_element(locator, return_multiple_elements, True)

    def get_element_by_type(self, method, value):
        """
        Returns an element for the given method and locator
        :param method:
        :param value:
        :return:
        """
        if method == By.ACCESSIBILITY_ID:
            return self.driver.find_element(By.ACCESSIBILITY_ID, value)
        elif method == By.CLASS_NAME:
            return self.driver.find_element(By.CLASS_NAME, value)
        elif method == By.ID:
            return self.driver.find_element(By.ID, value)
        elif method == By.XPATH:
            return self.driver.find_element(By.XPATH, value)
        elif method == By.NAME:
            return self.driver.find_element(By.NAME, value)
        elif method == By.IOS_CLASS_CHAIN:
            return self.driver.find_element(By.IOS_CLASS_CHAIN, value)
        else:
            raise Exception('Invalid locator method.')

    def get_elements_by_type(self, method, value):
        """
        Returns a list of elements based on provided locator.
        :param method:
        :param value:
        :return:
        """
        if method == By.ACCESSIBILITY_ID:
            return self.driver.find_elements(By.ACCESSIBILITY_ID, value)
        elif method == By.CLASS_NAME:
            return self.driver.find_elements(By.CLASS_NAME, value)
        elif method == By.ID:
            return self.driver.find_elements(By.ID, value)
        elif method == By.XPATH:
            return self.driver.find_elements(By.XPATH, value)
        elif method == By.NAME:
            return self.driver.find_elements(By.NAME, value)
        else:
            raise Exception('Invalid locator method.')

    def is_visible(self, locator):
        try:
            locator.is_displayed()
            return True
        except NoSuchElementException:
            return False

    def is_element_enabled(self, locator):
        try:
            logger.info(f"is_enabled: {locator.is_enabled()}")
            locator.is_enabled()
            return True
        except NoSuchElementException:
            return False

    def check_element_atributs(self, locator):
        logger.info("...")
        logger.info(f"is_enabled: {locator.is_enabled()}")
        logger.info(f"is_selected: {locator.is_selected()}")
        logger.info(f"is_displayed: {locator.is_displayed()}")
        logger.info(f'is_clickable: {locator.get_attribute("clickable")}')
        logger.info("...")

    def wait_visible(self, locator, timeout=global_timeout):
        """
              Wait for element to become visible.
              :param locator:
              :param timeout:
              :return:
              """
        i = 0
        while i != timeout:
            try:
                self.is_visible(locator)
                return locator
            except NoSuchElementException:
                sleep(1)
                i += 1
        raise Exception('Element never became visible: %s (%s)' % (locator))

    def wait_not_visible(self, locator, timeout=global_timeout):
        """
        Wait for element to become not visible.
        :param locator:
        :param timeout:
        :return:
        """
        count = 0
        while count != timeout:
            try:
                element_visible = self.is_visible(locator)
                if element_visible is False:
                    return True
            except NoSuchElementException:
                pass
            count += 1
            sleep(1)
        return False

    def wait_until_enabled(self, locator, timeout=global_timeout):
        count = 0
        while count != timeout:
            try:
                if locator.is_enabled():
                    return True
            except NoSuchElementException:
                sleep(1)
                count += 1
        return False

    def wait_for_text(self, locator, text, timeout=global_timeout, locator_from_list=False):
        """
        Wait for text to become visible.
        :param locator_from_list:
        :param locator:
        :param text:
        :param timeout:
        :return:
        """
        count = 0
        while count != timeout:
            try:
                if locator_from_list is False:
                    if locator.text.lower() == text.lower():
                        return True
                elif locator_from_list is True:
                    if locator.get_attribute("text").lower() == text.lower():
                        return True
            except NoSuchElementException:
                pass
            count += 1
            sleep(1)
        return False

    # clicks and taps
    def click(self, locator):
        element = self.wait_visible(locator)
        element.click()

    def tap(self, locator):
        element = self.wait_visible(locator)
        element.tap()

    def hide_keyboard(self):
        try:
            sleep(1)
            self.driver.hide_keyboard()
        except WebDriverException:
            pass

    def send_keys(self, locator, text):
        element = self.wait_visible(locator)
        element.send_keys(text)
        sleep(0.5)

    def clear(self, locator):
        element = self.wait_visible(locator)
        element.clear()
        sleep(0.5)

    # android scroll
    def android_scroll(self, locator):
        for _ in range(15):
            x = 950
            try:
                value = self.get_element(locator).is_displayed()
                if value is True:
                    break
            except NoSuchElementException:
                # swipe(start_x, start_y, end_x, end_y, duration)
                self.driver.swipe(470, 1400, 470, x, 330)
                self.driver.implicitly_wait(2)
                continue

    # ios scroll
    def ios_scroll(self, locator):
        el = self.wait_visible(locator)
        self.driver.execute_script('mobile: scroll', {"element": el, "toVisible": True})

    # common method to scroll in android & ios
    def scrolling(self, locator):
        self.android_scroll(locator)

    # get text
    def get_text(self, locator):
        return locator.text

    def tap_back_button(self):
        self.driver.back()

    def swipe_up(self):
        window_size = self.driver.get_window_size()
        center_x = window_size['width'] * 0.5
        center_y = window_size['height'] * 0.5
        where_to_x = center_x
        where_to_y = window_size['height'] - 0.1

        self.driver.swipe(center_x, center_y, where_to_x, where_to_y, duration=1000)

    def swipe_down(self, offset=0.5):
        window_size = self.driver.get_window_size()
        center_x = window_size['width'] * 0.5
        center_y = window_size['height'] * offset
        where_to_x = center_x
        where_to_y = window_size['height'] * 0.1

        self.driver.swipe(center_x, center_y, where_to_x, where_to_y, duration=1000)

    def hide_keyboard(self):
        """
        Hides keyboard if present.
        :return:
        """
        try:
            sleep(0.1)
            self.driver.hide_keyboard()
        except WebDriverException:
            pass

    def reset(self):
        self.driver.reset()

    def android_push_file(self, file):
        file_path = os.path.dirname(__file__) + f"/files/malware/{file}"
        destination_path = '/sdcard/'

        try:
            self.driver.push_file(destination_path, file_path)
            print("File has been successfully pushed to the device's internal storage.")
        except FileNotFoundError as e:
            logger.error("Error occurred while pushing the file:", str(e))

    def android_install_apk(self, file):
        file_path = os.path.dirname(__file__) + f"/files/malware/{file}"
        destination_path = '/sdcard/'

        try:
            self.driver.push_file(destination_path, file_path)
            self.driver.install_app(file_path)
            print("File has been successfully pushed to the device's internal storage.")
        except FileNotFoundError as e:
            logger.error("Error occurred while pushing the file:", str(e))
