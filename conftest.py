import pytest
from pages.qa_site_page import PracticeSite


@pytest.fixture
def home_page(page):
    obj = PracticeSite(page)
    obj.open()
    return obj


@pytest.fixture
def qa_site_page(page):
    return PracticeSite(page)