from pages.BasePage import BasePage


class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

