import pytest
import logging
from appium.options.android import UiAutomator2Options
from appium import webdriver
from pages.homesmartscreen import HomeSmartScreen

@pytest.fixture(scope="class")
def android(request):
    caps = {
        'platformName': 'Android',
        'platformVersion': '14',
        'automationName': 'UiAutomator2',
        'deviceName': 'j4lte',
        'appPackage': 'com.ikea.inter.homesmart.system2',
        'appActivity': 'com.ikea.system2.start.StartActivity',
        'udid': '42005f8dd4273523'
    }

    options = UiAutomator2Options()
    options.load_capabilities(caps)

    try:
        logging.info("Attempting to connect to Appium server at http://192.168.1.214:4273/wd/hub")
        driver = webdriver.Remote('http://192.168.1.214:4723/wd/hub', options=options)
        logging.info("Successfully connected to Appium server")
    except Exception as e:
        logging.error(f"Failed to connect to Appium server: {e}")
        raise e

    request.cls.driver = driver
    yield driver
    driver.quit()


def pytest_configure(config):
    config._metadata = {
        'Platform': 'Windows',
        'Python Version': '3.9'
    }
    logging.basicConfig(level=logging.INFO)


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logreport(report):
    if report.when == 'call':
        if report.failed:
            logging.error(f"Test failed: {report.nodeid}")
        elif report.passed:
            logging.info(f"Test passed: {report.nodeid}")


@pytest.fixture(scope="class")
def ikea_hub(android):
    return HomeSmartScreen(android)
