from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_registration_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_registration_input.fill('user.name@gmail.com')

    user_registration_input = page.get_by_test_id('registration-form-username-input').locator('input')
    user_registration_input.fill('username')

    password_registration_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_registration_input.fill('password')

    button_registration = page.get_by_test_id('registration-page-registration-button')
    button_registration.click()

    dashbord_title = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashbord_title).to_be_visible()
    expect(dashbord_title).to_have_text('Dashboard')
