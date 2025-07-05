from playwright.sync_api import sync_playwright, expect, Page
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    page = chromium_page_with_state
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    section_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(section_title).to_be_visible()
    expect(section_title).to_have_text('Courses')

    empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_view_icon).to_be_visible()

    empty_state_title = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(empty_state_title).to_be_visible()
    expect(empty_state_title).to_have_text('There is no results')

    empty_state_description = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(empty_state_description).to_be_visible()
    expect(empty_state_description).to_have_text('Results from the load test pipeline will be displayed here')

