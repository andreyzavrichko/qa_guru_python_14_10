from selene import browser, by, be


def test_selene():
    browser.open("/")
    browser.element("[data-target='qbsearch-input.inputButtonText']").click()
    browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example").press_enter()

    browser.element(by.link_text("eroshenkoam/allure-example")).click()

    browser.element("#issues-tab").click()

    browser.element(by.partial_text("С Новым Годом (2022)")).should(be.visible)
