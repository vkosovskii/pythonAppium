import os

import pytest
from appium import webdriver

from helpers.logger import gen_logger
from settings import Config

logger = gen_logger("Conftest")
config_data = Config()


def pytest_addoption(parser):
    """
    Set value from cmd: pytest test --device
    """
    parser.addoption('--device', action='store', default="emulator-5556")
    parser.addoption('--type', action='store', default="localTest")


def setup_module(self):
    self.driver.quit()


def pytest_generate_tests(metafunc):
    # This is called for every test. Only get/set command line arguments
    # if the argument is specified in the list of test "fixturenames".
    device_value = metafunc.config.option.device
    suit_type = metafunc.config.option.type
    config_data.set_config(device_value, suit_type)
    if 'device' in metafunc.fixturenames and device_value is not None:
        metafunc.parametrize("platform", [device_value])


@pytest.fixture
def driver() -> 'webdriver':
    config = config_data.get_config()
    logger.info(f"\nGet platform: {config}")
    logger.info("Init driver")
    desired_caps = {
        'platformName': config['platformName'],
        'platformVersion': config['platformVersion'],
        'deviceName': config['deviceName'],
        'automationName': config['automationName'],
        'appPackage': config['appPackage'],
        'appActivity': config['appActivity'],
        'app': config['app'],
        'noReset': config['noReset'],
        'fullReset': config['fullReset']
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(50)  # waits 5 seconds
    logger.info("Driver inited successfully")
    return driver
