from playwright.sync_api import expect
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):

    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    toolbar_text = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(toolbar_text).to_be_visible()
    expect(toolbar_text).to_have_text('Courses')

    title_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(title_text).to_be_visible()
    expect(title_text).to_have_text('There is no results')

    empty_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_icon).to_be_visible()

    description_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(description_text).to_be_visible()
    expect(description_text).to_have_text('Results from the load test pipeline will be displayed here')