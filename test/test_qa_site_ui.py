import re

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError, expect

# --------------------------------
r""" helper‑функція з fallback'ом №1, щоб стабільно перевіряти переходи, коли лінк може:
1.Відкритися в новій вкладці (popup) - основна перевірка
2.Відкритися в цій же вкладці - fallback, якщо перша перевірка хибна
"""

# def click_link_and_expect_url(page, click_fn, expected_url, popup_timeout_ms=2000, wait_state=None):
#     try:
#         with page.context.expect_page(timeout=popup_timeout_ms) as popup_info:
#             click_fn()
#         popup_page = popup_info.value
#         if wait_state:
#             popup_page.wait_for_load_state(wait_state)
#         expect(popup_page).to_have_url(expected_url)
#     except PlaywrightTimeoutError:
#         if wait_state:
#             page.wait_for_load_state(wait_state)
#         expect(page).to_have_url(expected_url)

r""" helper‑функція №2 без fallback'у,  перевіряє, коли лінк може:
Відкритися в новій вкладці (popup)
"""
def click_link_and_expect_new_tab(page, click_fn, expected_url, wait_state="domcontentloaded"):
    with page.context.expect_page() as new_page_info:
        click_fn()

    new_page = new_page_info.value
    new_page.wait_for_load_state(wait_state)
    expect(new_page).to_have_url(expected_url)

    return new_page
#--------------------------------


#-----------------header-----------------
def test_logo_visible(home_page):
    # home_page.get_logo()
    expect(home_page.logo).to_be_visible()
    assert home_page.get_logo().evaluate("img => img.complete && img.naturalWidth > 0") #("img => img.naturalWidth > 0")
def test_logo_has_link_to_home(home_page):
    expect(home_page.logo_link).to_have_attribute("href","/")
def test_logo_link_click_opens_home(home_page,page):
    home_page.click_logo_link()
    expect(page).to_have_url(home_page.URL + "/")
def test_logo_practice_site_is_visible(home_page):
    expect(home_page.logo_practice_site).to_be_visible()

def test_home_link(home_page,page):
    home_page.click_home_link()
    expect(page).to_have_url(re.compile(r"practice.qabrains.com"))
# def test_qa_topics_link(home_page,page):
#     click_link_and_expect_url(
#         page,
#         home_page.click_qa_topics,
#         re.compile(r"^https://qabrains\.com/topics/?$"),
#         wait_state="domcontentloaded",
#     )
def test_home_is_visible(home_page):
    expect(home_page.home_is_visible()).to_be_visible()

def test_qa_topics_opens_in_new_tab(home_page, page):
    click_link_and_expect_new_tab(
        page,
        home_page.click_qa_topics,
        re.compile(r"^https://qabrains\.com/topics/?$"),
    )
def test_qa_topics_target_and_href(home_page):
    expect(home_page.qa_topics).to_have_attribute("href", re.compile(r"^https://qabrains\.com/topics/?$"))
    expect(home_page.qa_topics).to_have_attribute("target", "_blank")
def test_qa_topics_is_visible(home_page):
    expect(home_page.qa_topics_is_visible()).to_be_visible()

def test_discussion_opens_in_new_tab(home_page,page):
    click_link_and_expect_new_tab(
        page,
        home_page.click_discussion,
        re.compile(r"^https://qabrains\.com/discussion/?$"),
    )
def test_discussion_target_and_href(home_page):
    expect(home_page.discussion).to_have_attribute("target", "_blank")
    expect(home_page.discussion).to_have_attribute("href",re.compile(r"^https://qabrains\.com/discussion/?$"))
def test_discussion_is_visible(home_page):
    expect(home_page.discussion_is_visible()).to_be_visible()

def test_tags_opens_in_new_tab(home_page,page):
    click_link_and_expect_new_tab(
        page,
        home_page.click_tags,
        re.compile(r"^https://qabrains\.com/tags/?$"),
    )
def test_tags_target_and_href(home_page):
    expect(home_page.tags).to_have_attribute("target", "_blank")
    expect(home_page.tags).to_have_attribute("href",re.compile(r"^https://qabrains\.com/tags/?$"))
def test_tags_is_visible(home_page):
    expect(home_page.tags_is_visible()).to_be_visible()

def test_jobs_opens_in_new_tab(home_page,page):
    click_link_and_expect_new_tab(
        page,
        home_page.click_jobs,
        re.compile(r"^https://qabrains\.com/jobs/?$"),
    )
def test_jobs_target_and_href(home_page):
    expect(home_page.jobs).to_have_attribute("target", "_blank")
    expect(home_page.jobs).to_have_attribute("href",re.compile(r"^https://qabrains\.com/jobs/?$"))
def test_jobs_is_visible(home_page):
    expect(home_page.jobs_is_visible()).to_be_visible()

def test_practice_site_opens_in_new_tab(home_page,page):
    click_link_and_expect_new_tab(
        page,
        home_page.click_practice_site,
        re.compile(r"^https://qabrains\.com/practice-site/?$"),
    )
def test_practice_site_target_and_href(home_page):
    expect(home_page.practice_site).to_have_attribute("target", "_blank")
    expect(home_page.practice_site).to_have_attribute("href",re.compile(r"^https://qabrains\.com/practice-site/?$"))
def test_practice_site_is_visible(home_page):
    expect(home_page.practice_site_is_visible()).to_be_visible()

def test_about_us_opens_in_new_tab(home_page,page):
    click_link_and_expect_new_tab(
        page,
        home_page.click_about_us,
        re.compile(r"^https://qabrains\.com/about/?$"),
    )
def test_about_us_target_and_href(home_page):
    expect(home_page.about_us).to_have_attribute("target", "_blank")
    expect(home_page.about_us).to_have_attribute("href",re.compile(r"^https://qabrains\.com/about/?$"))
def test_about_us_is_visible(home_page):
    expect(home_page.about_us_is_visible()).to_be_visible()

def test_header_navigation_is_visible(home_page):
    expect(home_page.get_header_navigation()).to_be_visible()
def test_header_navigation_is_hidden(home_page,page):
    page.set_viewport_size({"width": 1023, "height": 812})
    expect(home_page.get_header_navigation()).to_be_hidden()

def test_sign_in_target_and_href(home_page):
    expect(home_page.sign_in).to_have_attribute("target", "_blank")
    expect(home_page.sign_in).to_have_attribute("href",re.compile(r"^https://qabrains\.com/auth/login/?$"))
def test_sign_in_opens_in_new_tab(home_page,page):
    click_link_and_expect_new_tab(
        page,
        home_page.click_sign_in,
        re.compile(r"^https://qabrains\.com/auth/login/?$")
    )
def test_sign_in_is_visible(home_page):
    expect(home_page.sign_in_is_visible()).to_be_visible()
#-----------------header-----------------


#-----------------sidebar----------------
def test_sidebar_button_is_visible(home_page, page):
    page.set_viewport_size({"width": 1023, "height": 812})  # Для зменшення розміру екрана
    expect(home_page.sidebar_button_is_visible()).to_be_visible()
def test_sidebar_menu_item_is_visible(home_page,page):
    page.set_viewport_size({"width": 1023, "height": 812})
    home_page.click_sidebar_button()
    expect(home_page.get_sidebar()).to_be_visible()

def test_demo_module_is_visible(home_page):
    expect(home_page.demo_module_is_visible()).to_be_visible()
def test_demo_site_is_visible(home_page):
    expect(home_page.demo_site_is_visible()).to_be_visible()

def test_user_authentication_button(home_page):
    expect(home_page.user_authentication_button).to_be_visible()
    home_page.click_user_authentication_button()

    expect(home_page.demo_module_login_button).to_be_hidden()
    expect(home_page.demo_module_registration_button).to_be_hidden()
    expect(home_page.demo_module_forgot_password_button).to_be_hidden()

    home_page.click_user_authentication_button()

    expect(home_page.demo_module_login_button).to_be_visible()
    expect(home_page.demo_module_registration_button).to_be_visible()
    expect(home_page.demo_module_forgot_password_button).to_be_visible()
#-----------------sidebar----------------


# -----------------User Authentication (Login)----------------
def test_user_authentication_and_login_pages_is_visible(home_page):
    expect(home_page.get_user_authentication()).to_be_visible()
    expect(home_page.get_login_page()).to_be_visible()

def test_email_and_password_and_login_button_is_visible(home_page):
    expect(home_page.email_input).to_be_visible()
    expect(home_page.password_input).to_be_visible()
    expect(home_page.login_button).to_be_visible()

def test_the_work_email_password_login_button(home_page):
    home_page.enter_email("qa_testers@qabrains.com")
    home_page.enter_password("Password123")
    home_page.click_login_button()

    expect(home_page.get_login_successful_text()).to_be_visible()
    expect(home_page.get_congratulations_text()).to_be_visible()
# -----------------User Authentication (Login)----------------

# -----------------User Authentication (Registration)----------------
def test_registration_name(home_page):
    home_page.click_registration_button()

  # -------------------text----------------------
    expect(home_page.get_registration_name()).to_be_visible()
    expect(home_page.get_registration_select_country()).to_be_visible()
    expect(home_page.get_registration_account_type()).to_be_visible()
    expect(home_page.get_registration_email()).to_be_visible()
    expect(home_page.get_registration_password()).to_be_visible()
    expect(home_page.get_registration_confirm_password()).to_be_visible()
  # -------------------text----------------------

  # -------------------select/input fields----------------------
    expect(home_page.get_name_inputs()).to_be_visible()
    home_page.fill_name_inputs()
    expect(home_page.name_input).to_be_visible()

    expect(home_page.get_select_country()).to_be_visible()
    home_page.select_country_select()
    home_page.click_country_list()
    expect(home_page.get_select_country()).to_have_value("Angola")
  # -------------------select/input fields----------------------
# -----------------User Authentication (Registration)----------------