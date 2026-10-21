import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

from pages.login_page import LoginPage
from data.users import Users


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = ChromeOptions()

        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
            "profile.default_content_setting_values.notifications": 2,
            "autofill.profile_enabled": False,
        }
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-notifications")

        browser = webdriver.Chrome(options=options)
    else:
        profile = FirefoxProfile()
        profile.set_preference("dom.webnotifications.enabled", False)
        profile.set_preference("signon.rememberSignons", False)

        options = FirefoxOptions()
        options.profile = profile

        browser = webdriver.Firefox(options=options)

    browser.maximize_window()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


@pytest.fixture
def authorized_user(driver):
    login = LoginPage(driver)
    login.open()
    login.login(Users.EXISTING["email"], Users.EXISTING["password"])
    return Users.EXISTING
