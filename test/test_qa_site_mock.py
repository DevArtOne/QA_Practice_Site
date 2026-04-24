from playwright.sync_api import expect
import json

def test_mock_module_home_page(qa_site_page, page):
    def mock_module_home_page(route):
        mock_data = {
            "module": [
                {
                    "key": "auth",
                    "title": "Auth Module",
                    "icon": "https://qabrain-prod.s3.ap-south-1.amazonaws.com/content-managements/practice_page/icons/login.svg",
                    "is_active": True,
                    "is_disable": False,
                    "items": [
                        {
                            "key": "login",
                            "label": "John",
                            "icon": "https://qabrain-prod.s3.ap-south-1.amazonaws.com/content-managements/practice_page/icons/login.svg",
                            "is_active": True,
                            "is_disable": False
                        },
                        {
                            "key": "registration",
                            "label": "Nat",
                            "icon": "https://qabrain-prod.s3.ap-south-1.amazonaws.com/content-managements/practice_page/icons/registration.svg",
                            "is_active": True,
                            "is_disable": False
                        },
                        {
                            "key": "forgot-password",
                            "label": "Jack",
                            "icon": "https://qabrain-prod.s3.ap-south-1.amazonaws.com/content-managements/practice_page/icons/forgot-password.svg",
                            "is_active": True,
                            "is_disable": False
                        }
                    ]
                }
            ],
            "site": []
        }

        route.fulfill(
            status=200,
            content_type="application/json",
            body= json.dumps(mock_data)
        )

    page.route("**/api/v1/component/categories", mock_module_home_page)
    qa_site_page.open()
    expect(page.get_by_text("John").first).to_be_visible()
    expect(page.get_by_text("Nat").first).to_be_visible()
    expect(page.get_by_text("Jack").first).to_be_visible()
    #page.pause() #для зупинки тесту, щоб браузер не закрився автоматично