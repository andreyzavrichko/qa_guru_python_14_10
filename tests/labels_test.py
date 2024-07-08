import allure
from allure_commons.types import Severity
from selene import browser, by, be


def test_dynamic_labels():
    allure.dynamic.tag("WEB")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("Проверка отображения названия Issue")
    allure.dynamic.link("https://github.com", name="Testing")
    browser.open("/")
    browser.element("[data-target='qbsearch-input.inputButtonText']").click()
    browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example").press_enter()

    browser.element(by.link_text("eroshenkoam/allure-example")).click()

    browser.element("#issues-tab").click()

    browser.element(by.partial_text("С Новым Годом (2022)")).should(be.visible)


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "Аркадий Укупник")
@allure.feature("Задачи в репозитории")
@allure.story("Проверка отображения названия Issue")
@allure.link("https://github.com", name="Testing")
def test_decorator_labels():
    browser.open("/")
    browser.element("[data-target='qbsearch-input.inputButtonText']").click()
    browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example").press_enter()

    browser.element(by.link_text("eroshenkoam/allure-example")).click()

    browser.element("#issues-tab").click()

    browser.element(by.partial_text("С Новым Годом (2022)")).should(be.visible)
