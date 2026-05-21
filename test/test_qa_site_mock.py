from playwright.sync_api import expect
import json

def test_mock_module_home_page(qa_site_home_page, page):
    def mock_module_home_page(route):
        mock_data = {
            "module": [
                {
                    "key": "auth",
                    "title": "User LOOSER",
                    "icon": "",
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
                        },
                        {
                            "key": "bubeishion",
                            "label": "Nika",
                            "icon": "https://qabrain-prod.s3.ap-south-1.amazonaws.com/content-managements/practice_page/icons/registration.svg",
                            "is_active": True,
                            "is_disable": False
                        }
                    ]
                },
                {
                    "key": "form-submission",
                    "title": "Form UNIFORM",
                    "icon": "https://qabrain-prod.s3.ap-south-1.amazonaws.com/content-managements/practice_page/icons/form-submission.svg",
                    "is_active": True,
                    "is_disable": False
                },
                {
                    "key": "drag-drop",
                    "title": "Drag and Duck",
                    "icon": "https://qabrain-prod.s3.ap-south-1.amazonaws.com/content-managements/practice_page/icons/drag-drop.svg",
                    "is_active": True,
                    "is_disable": False
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
    qa_site_home_page.open()

    expect(page.get_by_text("John").first).to_be_visible()
    expect(page.get_by_text("Nat").first).to_be_visible()
    expect(page.get_by_text("Jack").first).to_be_visible()
    expect(page.get_by_text("User LOOSER").first).to_be_visible()
    expect(page.get_by_text("Form UNIFORM").first).to_be_visible()
    expect(page.get_by_text("Drag and Duck").first).to_be_visible()
    page.pause() #для зупинки тесту, щоб браузер не закрився автоматично


def test_mock_site_home_page(qa_site_home_page, page):
    def mock_site_home_page(route):
        mock_data = {
            "module": [],
            "site": [
                {
                    "key": "ecommerce-site",
                    "title": "E-KUKUMBER Site",
                    "icon": "https://qabrain-prod.s3.ap-south-1.amazonaws.com/content-managements/practice_page/icons/ecommerce-site.svg",
                    "is_active": True,
                    "is_disable": False
                },
                {
                    "key": "booking-site",
                    "title": "Booking LIBRARY",
                    "icon": "",
                    "is_active": True,
                    "is_disable": True
                }
            ]
        }

        route.fulfill(
            status=200,
            content_type = "application/json",
            body= json.dumps(mock_data)
        )

    page.route("**/api/v1/component/categories", mock_site_home_page)
    qa_site_home_page.open()

    expect(page.get_by_text("E-KUKUMBER Site").first).to_be_visible()
    expect(page.get_by_text("Booking LIBRARY").first).to_be_visible()
    page.pause()



def test_mock_categories_with_handler_route_request(qa_site_home_page, page):
    def handler(route, request):
        # Перевіряємо сам запит перед мок-відповіддю
        assert request.method == "GET"
        assert "/api/v1/component/categories" in request.url

        mock_data = {
            "module": [
                {
                    "key": "auth",
                    "title": "User Authentication",
                    "icon": "",
                    "is_active": True,
                    "is_disable": False,
                    "items": [
                        {
                            "key": "login",
                            "label": "Login",
                            "icon": "",
                            "is_active": True,
                            "is_disable": False
                        }
                    ]
                }
            ],
            "site": [
                {
                    "key": "ecommerce-site",
                    "title": "Ecommerce Site",
                    "icon": "",
                    "is_active": True,
                    "is_disable": False
                }
            ]
        }

        route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps(mock_data)
        )

    page.route("**/api/v1/component/categories", handler)
    qa_site_home_page.open()

    expect(page.get_by_text("User Authentication").first).to_be_visible()
    expect(page.get_by_text("Login").first).to_be_visible()
    expect(page.get_by_text("Ecommerce Site").first).to_be_visible()
    page.pause()