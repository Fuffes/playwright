from configuration import PASSWORD
from pages.BasePage import BasePage


class LoginPage(BasePage):


    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.login_field = "//input[@id='user-name']"
        self.password_field = "//input[@id='password']"
        self.login_btn = "//input[@id='login-button']"
        self.error_message = "//div[@class = 'error-message-container error']"


    def enter_login(self, login):
        self.enter_text(self.login_field, login)

    def enter_password(self):
        self.enter_text(self.password_field, PASSWORD)

    def press_btn(self):
        self.click_element(locator=self.login_btn)

    def errorMess_equal_to(self, expected_message):
        actual_message = self.page.wait_for_selector(self.error_message)
        es = actual_message.inner_text()
        print(es)
