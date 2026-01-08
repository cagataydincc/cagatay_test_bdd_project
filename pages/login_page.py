from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("[data-test=\"username\"]")
        self.password = page.locator("[data-test=\"password\"]")
        self.login_button = page.locator("[data-test=\"login-button\"]")

    def goto(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, user, pwd):
        self.username.fill("standard_user")
        self.password.fill("secret_sauce")
        self.login_button.click()




