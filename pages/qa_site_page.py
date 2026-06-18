import re

from playwright.sync_api import Page


class PracticeSite:
    URL = 'https://practice.qabrains.com'

    def __init__(self, page: Page):
        self.page = page


#-----------------header-----------------
        self.logo = page.get_by_alt_text("Logo").first
        self.logo_link = page.locator('a[href="/"]').filter(has=self.logo).first
        self.logo_practice_site = page.locator("small").filter(has_text="Practice Site").first

        self.home = page.get_by_role('link', name='home')
        self.qa_topics = page.get_by_role('link', name=re.compile(r"QA Topics"))
        self.discussion = page.locator("#nav").get_by_role('link', name=re.compile(r"Discussion"))
        self.tags = page.locator("#nav").get_by_role('link', name=re.compile(r"Tags"))
        self.jobs = page.locator("#nav").get_by_role('link', name=re.compile(r"Jobs"))
        self.practice_site = page.locator("#nav").get_by_role('link', name=re.compile(r"Practice Site"))
        self.about_us = page.locator("#nav").get_by_role('link', name=re.compile(r"About Us"))

        self.header_navigation = page.locator("#nav")

        self.sign_in = page.get_by_role('link', name=re.compile(r"Sign In"))
#-----------------header-----------------

#-----------------sidebar----------------
        self.sidebar_button = page.locator("#page-header").get_by_role("button").first
        self.sidebar = page.locator("#page-sidebar")

        self.demo_module = page.locator("#demo-module")
        self.demo_module_heading = self.demo_module.get_by_role("heading", level=3).filter(has_text="Demo Module").first
        self.user_authentication_button = self.demo_module.get_by_role("menuitem", name="User Authentication")
        self.demo_module_login_button = self.demo_module.get_by_role("menuitem", name="Login")
        self.demo_module_registration_button = self.demo_module.get_by_role("menuitem", name="Registration")
        self.demo_module_forgot_password_button = self.demo_module.get_by_role("menuitem", name="Forgot Password")

        self.demo_site = page.locator("#demo-site")
        self.demo_site_heading = self.demo_site.get_by_role("heading", level=3).filter(has_text="Demo Site").first

# -----------------sidebar----------------

# -----------------User Authentication (Login)----------------
        self.user_authentication = page.get_by_role("heading", level=2).filter(has_text="User Authentication").first
        self.login_page = page.locator("[data-slot='alert-title']").filter(has_text="Login Page").first
        self.email_input = page.get_by_role("textbox", name="email")
        self.password_input = page.get_by_role("textbox", name="password")
        self.login_button = page.get_by_role("button", name="login")

        self.login_successful = page.get_by_role("heading", level=2).filter(has_text="Login Successful").first
        self.congratulations = page.get_by_role("paragraph").filter(has_text=re.compile(r"Congratulations", re.IGNORECASE)).first
# -----------------User Authentication (Login)----------------

# -----------------User Authentication (Registration)----------------
        self.registration_button = page.get_by_role("menuitem", name="registration")

    #-------------------text----------------------
        self.registration_name = page.get_by_label("Name")
        self.registration_select_country = page.get_by_label("Select Country")
        self.registration_account_type = page.get_by_label("Account Type")
        self.registration_email = page.get_by_label("Email")
        self.registration_password = page.get_by_label("Password").nth(0)
        self.registration_confirm_password = page.get_by_label("Confirm Password")
    #-------------------text----------------------

    #-------------------select/input fields----------------------
        self.name_input = page.get_by_role("textbox", name="name")
        self.select_country = page.get_by_role("combobox", name="country")
        self.account_type_select = page.get_by_role("combobox", name="account")
        self.email_input = page.get_by_role("textbox", name="email")
        self.password_input = page.get_by_role("textbox", name="password")
        self.confirm_password_input = page.get_by_role("textbox", name="confirm_password")
        self.country_list = page.get_by_role("option", name="Angola")
    #-------------------select/input fields----------------------

# -----------------User Authentication (Registration)----------------



    def open(self):
        self.page.goto(self.URL)

#-----------------header-----------------
    def get_logo(self):
        return self.logo
    def click_logo_link(self):
        self.logo_link.click()
    def get_logo_practice_site(self):
        return self.logo_practice_site

    def click_home_link(self):
        self.home.click()
    def home_is_visible(self):
        return self.home

    def click_qa_topics(self):
        self.qa_topics.click()
    def qa_topics_is_visible(self):
        return self.qa_topics

    def click_discussion(self):
        self.discussion.click()
    def discussion_is_visible(self):
        return self.discussion

    def click_tags(self):
        self.tags.click()
    def tags_is_visible(self):
        return self.tags

    def click_jobs(self):
        self.jobs.click()
    def jobs_is_visible(self):
        return self.jobs

    def click_practice_site(self):
        self.practice_site.click()
    def practice_site_is_visible(self):
        return self.practice_site

    def click_about_us(self):
        self.about_us.click()
    def about_us_is_visible(self):
        return self.about_us

    def get_header_navigation(self):
        return self.header_navigation

    def click_sign_in(self):
        self.sign_in.click()
    def sign_in_is_visible(self):
        return self.sign_in
#-----------------header-----------------

# -----------------sidebar----------------
    def sidebar_button_is_visible(self):
        return self.sidebar_button
    def click_sidebar_button(self):
        self.sidebar_button.click()
    def get_sidebar(self):
        return self.sidebar

    def demo_module_is_visible(self):
        return self.demo_module_heading
    def demo_site_is_visible(self):
        return self.demo_site_heading
    def click_user_authentication_button(self):
        self.user_authentication_button.click()
#-----------------sidebar----------------


# -----------------User Authentication (Login)----------------
    def get_user_authentication(self):
        return self.user_authentication
    def get_login_page(self):
        return self.login_page

    def enter_email(self, text: str):
        self.email_input.fill(text)
    def enter_password(self, text: str):
        self.password_input.fill(text)

    def click_login_button(self):
        self.login_button.click()

    def get_login_successful_text(self):
        return self.login_successful
    def get_congratulations_text(self):
        return self.congratulations
# -----------------User Authentication (Login)----------------

# -----------------User Authentication (Registration)----------------
    def click_registration_button(self):
        self.registration_button.click()

  # -------------------text----------------------
    def get_registration_name(self):
        return self.registration_name
    def get_registration_select_country(self):
        return self.registration_select_country
    def get_registration_account_type(self):
        return self.registration_account_type
    def get_registration_email(self):
        return self.registration_email
    def get_registration_password(self):
        return self.registration_password
    def get_registration_confirm_password(self):
        return self.registration_confirm_password
  # -------------------text----------------------

  # -------------------select/input fields----------------------
    def get_name_inputs(self):
        return self.name_input
    def fill_name_inputs(self):
        self.name_input.fill("Jhon Doe")

    def get_select_country(self):
        return self.select_country
    def select_country_select(self):
        self.select_country.click()
    def get_country_list(self):
        return self.country_list
    def click_country_list(self):
        self.select_country.select_option("Angola")
  # -------------------select/input fields----------------------
# -----------------User Authentication (Registration)----------------


