import pytest
from selenium import webdriver
import os
import re
from utilities.customLogger import LogGen

# Fixture to generate logger per test and attach to node
@pytest.fixture
def test_logger(request):
    #test_name = re.sub(r'\W+', '_', request.node.nodeid)
    test_name = request.node.name
    logger = LogGen.loggen(test_name)
    request.node._logger = logger  # Attach logger to node
    return logger

# Add custom CLI option
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

# WebDriver fixture with logger integration
@pytest.fixture(name='setup', scope='function')
def setup(request, test_logger):
    logger = test_logger
    logger.info(f"********* Starting Test: {request.node.name} ***********")

    browser = request.config.getoption("--browser").lower()

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    request.node.driver = driver  # Attach driver to node
    yield driver
    driver.quit()

# Hook to capture test results and take screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    logger = getattr(item, "_logger", None)

    if rep.when == 'call' and logger:
        if rep.failed:
            testcase_name = item.name
            logger.error(f"*************** {testcase_name} FAILED *********************")

            driver = getattr(item, 'driver', None)

            if driver:
                project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                screenshot_dir = os.path.join(project_root, 'tempdirectory')
                os.makedirs(screenshot_dir, exist_ok=True)

                screenshot_path = os.path.join(screenshot_dir, f"{testcase_name}.png")
                if os.path.exists(screenshot_path):
                    os.remove(screenshot_path)

                driver.save_screenshot(screenshot_path)
        else:
            logger.info(f"*************** {item.name} {rep.outcome.upper()} *********************")

# Add custom metadata
def pytest_configure(config):
    config._metadata['Project Name'] = "nop Commerce"
    config._metadata['Module Name'] = "Customers"
    config._metadata['Tester'] = "Anuj"

# Optionally remove some metadata
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("Plugins", None)
    metadata.pop("Python", None)
