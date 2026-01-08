import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture #Fixture = Testten önce hazırlık yapan ve test bitince temizlik yapan yardımcı fonksiyon.
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

# ✔️ Testten önce
# Playwright başlatır
# Chromium açar
# Sayfa oluşturur
#
# ✔️ Test sırasında
# Sayfa testin içine verilir (page değişkeni)
#
# ✔️ Test bitince
# Sayfa kapanır
# Context kapanır
# Browser kapanır
