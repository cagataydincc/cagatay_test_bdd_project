from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import Page
from pages.login_page import LoginPage

# Scenario'ları yükle
scenarios('features/login.feature')

@given('kullanıcı login sayfasındadır')
def kullanici_login_sayfasinda(page: Page):
    login_page = LoginPage(page)
    login_page.goto()


@when(parsers.parse('kullanıcı "{username}" ve "{password}" ile giriş yapar'))
def kullanici_giris_yapar(page: Page, username: str, password: str):
    login_page = LoginPage(page)
    login_page.username.fill(username)
    login_page.password.fill(password)
    login_page.login_button.click()



@then('kullanıcı başarıyla giriş yapmış olur')
def kullanici_basariyla_giris_yapar(page: Page):
    # Giriş sonrası görünecek bir element kontrol edilebilir
    title = page.locator("[data-test=\"title\"]")
    assert title.text_content() == "Products"  # ❌ text_content() parametre almaz
                                               # 1. text_content() metni döndürür
                                               # 2. == ile karşılaştırır

