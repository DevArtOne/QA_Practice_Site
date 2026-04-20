import re

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError, expect

# --------------------------------
r""" helper‑функція, щоб стабільно перевіряти переходи, коли лінк може:
1.Відкритися в новій вкладці (popup)
2.Відкритися в цій же вкладці"""

def click_link_and_expect_url(page, click_fn, expected_url, popup_timeout_ms=2000, wait_state=None):
    try:
        with page.context.expect_page(timeout=popup_timeout_ms) as popup_info:
            click_fn()
        popup_page = popup_info.value
        if wait_state:
            popup_page.wait_for_load_state(wait_state)
        expect(popup_page).to_have_url(expected_url)
    except PlaywrightTimeoutError:
        if wait_state:
            page.wait_for_load_state(wait_state)
        expect(page).to_have_url(expected_url)
#--------------------------------


#-----------------header-----------------
def test_logo_visible(home_page):
    # home_page.get_logo()
    expect(home_page.logo).to_be_visible()
    assert home_page.get_logo().evaluate("img => img.naturalWidth > 0")

def test_home_link(home_page,page):
    home_page.click_home_link()
    expect(page).to_have_url(re.compile(r"practice.qabrains.com"))
def test_qa_topics_link(home_page,page):
    click_link_and_expect_url(
        page,
        home_page.click_qa_topics,
        re.compile(r"^https://qabrains\.com/topics/?$"),
        wait_state="domcontentloaded",
    )
def test_qa_topics_target_and_href(home_page,page):
    expect(home_page.qa_topics).to_have_attribute("href", re.compile(r"^https://qabrains\.com/topics/?$"))
    expect(home_page.qa_topics).to_have_attribute("target", "_blank")
def test_discussion_link(home_page,page):
    click_link_and_expect_url(
        page,
        home_page.click_discussion,
        re.compile(r"^https://qabrains\.com/discussion/?$"),
        wait_state="domcontentloaded",
    )
def test_discussion_target_and_href(home_page,page):
    expect(home_page.discussion).to_have_attribute("target", "_blank")
    expect(home_page.discussion).to_have_attribute("href",re.compile(r"^https://qabrains\.com/discussion/?$"))
def test_tags_link(home_page,page):
    click_link_and_expect_url(
        page,
        home_page.click_tags,
        re.compile(r"^https://qabrains\.com/tags/?$"),
        wait_state="domcontentloaded",
    )
def test_tags_target_and_href(home_page,page):
    expect(home_page.tags).to_have_attribute("target", "_blank")
    expect(home_page.tags).to_have_attribute("href",re.compile(r"^https://qabrains\.com/tags/?$"))
def test_jobs_link(home_page,page):
    click_link_and_expect_url(
        page,
        home_page.click_jobs,
        re.compile(r"^https://qabrains\.com/jobs/?$"),
        wait_state="domcontentloaded",
    )
def test_jobs_target_and_href(home_page,page):
    expect(home_page.jobs).to_have_attribute("target", "_blank")
    expect(home_page.jobs).to_have_attribute("href",re.compile(r"^https://qabrains\.com/jobs/?$"))
def test_practice_site_link(home_page,page):
    click_link_and_expect_url(
        page,
        home_page.click_practice_site,
        re.compile(r"^https://qabrains\.com/practice-site/?$"),
        wait_state="domcontentloaded",
    )
def test_practice_site_target_and_href(home_page,page):
    expect(home_page.practice_site).to_have_attribute("target", "_blank")
    expect(home_page.practice_site).to_have_attribute("href",re.compile(r"^https://qabrains\.com/practice-site/?$"))
def test_about_us_link(home_page,page):
    click_link_and_expect_url(
        page,
        home_page.click_about_us,
        re.compile(r"^https://qabrains\.com/about/?$"),
        wait_state="domcontentloaded",
    )
def test_about_us_target_and_href(home_page,page):
    expect(home_page.about_us).to_have_attribute("target", "_blank")
    expect(home_page.about_us).to_have_attribute("href",re.compile(r"^https://qabrains\.com/about/?$"))
#-----------------header-----------------
