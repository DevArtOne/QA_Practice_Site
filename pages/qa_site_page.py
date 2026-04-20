import re

from playwright.sync_api import Page


class PracticeSite:
    URL = 'https://practice.qabrains.com'

    def __init__(self, page: Page):
        self.page = page


#-----------------header-----------------
        self.logo = page.locator(".inline-flex.items-end.gap-1").get_by_role("img")

        self.home = page.get_by_role('link', name='home')
        self.qa_topics = page.get_by_role('link', name=re.compile(r"QA Topics"))
        self.discussion = page.locator("#nav").get_by_role('link', name=re.compile(r"Discussion"))
        self.tags = page.locator("#nav").get_by_role('link', name=re.compile(r"Tags"))
        self.jobs = page.locator("#nav").get_by_role('link', name=re.compile(r"Jobs"))
        self.practice_site = page.locator("#nav").get_by_role('link', name=re.compile(r"Practice Site"))
        self.about_us = page.locator("#nav").get_by_role('link', name=re.compile(r"About Us"))

#-----------------header-----------------








    def open(self):
        self.page.goto(self.URL)

#-----------------header-----------------
    def get_logo(self):
        return self.logo

    def click_home_link(self):
        self.home.click()
    def click_qa_topics(self):
        self.qa_topics.click()
    def click_discussion(self):
        self.discussion.click()
    def click_tags(self):
        self.tags.click()
    def click_jobs(self):
        self.jobs.click()
    def click_practice_site(self):
        self.practice_site.click()
    def click_about_us(self):
        self.about_us.click()
#-----------------header-----------------
