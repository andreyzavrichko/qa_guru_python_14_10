import allure
from selene import browser, by, be


def test_dynamic_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("/")

    with allure.step("Ищем репозиторий"):
        browser.element("[data-target='qbsearch-input.inputButtonText']").click()
        browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example").press_enter()

    with allure.step("Переходим по ссылке репозитория"):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем таб Issues"):
        browser.element("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с текстом С Новым Годом (2022)"):
        browser.element(by.partial_text("С Новым Годом (2022)")).should(be.visible)


def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_name("С Новым Годом (2022)")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("/")


@allure.step("Ищем репозитория {repo}")
def search_for_repository(repo):
    browser.element("[data-target='qbsearch-input.inputButtonText']").click()
    browser.element("#query-builder-test").send_keys(repo).press_enter()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    browser.element("#issues-tab").click()


@allure.step("Проверяем наличие Issue с названием {name}")
def should_see_issue_with_name(name):
    browser.element(by.partial_text(name)).click()
