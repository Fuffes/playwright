

class BasePage():
    def __init__(self,page):
        self.page = page

    def click_element(self, locator):
        element = self.page.wait_for_selector(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.page.wait_for_selector(locator)
        element.fill(text)

    def navigate(self, URL):
        self.page.goto(URL)

