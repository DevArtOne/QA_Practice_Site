from conftest import qa_site_home_page


def test_home_demo_module_site_api_request(qa_site_home_page, page):
    with page.expect_request("**/api/v1/component/categories") as request_info:
        qa_site_home_page.open()

    request = request_info.value
    assert request.method == "GET"

def test_home_module_site_api_response(qa_site_home_page, page):
    with page.expect_response("**/api/v1/component/categories") as response_info:
        qa_site_home_page.open()

    response = response_info.value
    assert response.status == 200

    data = response.json()
    assert isinstance(data.get("module"), list)
    assert isinstance(data.get("site"), list)
    assert data["module"]
    assert data["site"]

    # assert "key" in data["module"][0] #Це означає: “чи є ключ items у першому об’єкті списку module”.
    first_module = data["module"][0]
    required_module_fields = {"key", "title", "icon", "is_active", "is_disable"}  #, "items"
    assert required_module_fields.issubset(first_module) #Це перевірка, що всі потрібні ключі є в словнику first_module. Тобто майже те саме, що: assert "key" in first_module

    assert isinstance(first_module["key"], str)
    assert isinstance(first_module["title"], str)
    assert isinstance(first_module["icon"], str)
    assert isinstance(first_module["is_active"], bool)
    assert isinstance(first_module["is_disable"], bool)
    assert isinstance(first_module["items"], list)

    assert first_module["key"]
    assert first_module["title"]
    assert first_module["items"]

    first_item = first_module["items"][0]
    required_item_fields = {"key", "label", "icon", "is_active", "is_disable"}
    assert required_item_fields.issubset(first_item)

    assert isinstance(first_item["key"], str)
    assert isinstance(first_item["label"], str)
    assert isinstance(first_item["icon"], str)
    assert isinstance(first_item["is_active"], bool)
    assert isinstance(first_item["is_disable"], bool)

    assert first_item["key"]
    assert first_item["label"]

    assert all(required_module_fields.issubset(module) for module in data["module"])
    assert all("key" in module for module in data["module"]) #перевіряє, що всі елементи мають ключ key (використовувати коли потрібно перевірити один ключ)
    assert all(required_item_fields.issubset(module) for module in data["module"][0]["items"]) #Перевіряє, що всі елементи мають всі ці ключі{"key", "label", "icon", "is_active", "is_disable"}


    first_site_item = data["site"][0]
    required_module_site_fields = {"key", "title", "icon", "is_active", "is_disable"}
    assert required_module_site_fields.issubset(first_site_item)

    assert isinstance(first_site_item["key"], str)
    assert isinstance(first_site_item["title"], str)
    assert isinstance(first_site_item["icon"], str)
    assert isinstance(first_site_item["is_active"], bool)
    assert isinstance(first_site_item["is_disable"], bool)

    assert all(required_module_site_fields.issubset(site_item) for site_item in data["site"])
