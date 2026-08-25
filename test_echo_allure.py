import allure
import requests

BASE_URL = "https://postman-echo.com"


@allure.title("GET /get - возврат query параметров")
@allure.description("Тест проверяет, что GET /get возвращает query-параметры в поле args")
@allure.feature("Echo API")
@allure.story("GET /get")
@allure.severity(allure.severity_level.NORMAL)
def test_get_returns_query_params():
    """GET /get должен вернуть квери-параметры в поле args."""
    url = f"{BASE_URL}/get"
    params = {"foo": "bar", "num": "1"}
    
    with allure.step("Отправка GET запроса с параметрами"):
        allure.attach(f"URL: {url}", name="Request URL", attachment_type=allure.attachment_type.TEXT)
        allure.attach(str(params), name="Query Params", attachment_type=allure.attachment_type.TEXT)
        response = requests.get(url, params=params)
    
    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    with allure.step("Проверка возвращённых параметров"):
        data = response.json()
        assert data["args"]["foo"] == "bar"
        assert data["args"]["num"] == "1"


@allure.title("POST /post - возврат JSON тела")
@allure.description("Тест проверяет, что POST /post с JSON возвращает тело в поле json")
@allure.feature("Echo API")
@allure.story("POST /post")
@allure.severity(allure.severity_level.CRITICAL)
def test_post_returns_json_body():
    """POST /post c JSON должен вернуть тело в поле json."""
    url = f"{BASE_URL}/post"
    payload = {"name": "Olga", "course": "Python"}
    
    with allure.step("Подготовка JSON payload"):
        allure.attach(str(payload), name="Request Body", attachment_type=allure.attachment_type.JSON)
    
    with allure.step("Отправка POST запроса с JSON"):
        allure.attach(f"URL: {url}", name="Request URL", attachment_type=allure.attachment_type.TEXT)
        response = requests.post(url, json=payload)
    
    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200
    
    with allure.step("Проверка возвращённого JSON"):
        data = response.json()
        assert data["json"] == payload


@allure.title("POST /post - возврат form-data")
@allure.description("Тест проверяет, что POST /post с form-data возвращает поля в поле form")
@allure.feature("Echo API")
@allure.story("POST /post")
@allure.severity(allure.severity_level.NORMAL)
def test_post_returns_form_data():
    """POST /post c form-data должен вернуть поля в поле form."""
    url = f"{BASE_URL}/post"
    payload = {"field1": "value1", "field2": "value2"}
    
    with allure.step("Подготовка form-data"):
        allure.attach(str(payload), name="Form Data", attachment_type=allure.attachment_type.TEXT)
    
    with allure.step("Отправка POST запроса с form-data"):
        response = requests.post(url, data=payload)
    
    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200
    
    with allure.step("Проверка возвращённых данных"):
        data = response.json()
        assert data["form"]["field1"] == "value1"
        assert data["form"]["field2"] == "value2"


@allure.title("GET /get - эхо заголовков")
@allure.description("Тест проверяет, что GET /get отражает пользовательские заголовки")
@allure.feature("Echo API")
@allure.story("GET /get")
@allure.severity(allure.severity_level.NORMAL)
def test_get_echoes_headers():
    """GET /get должен отразить пользовательский заголовок в headers."""
    url = f"{BASE_URL}/get"
    headers = {"X-Custom-Header": "my-header"}
    
    with allure.step("Подготовка заголовков"):
        allure.attach(str(headers), name="Request Headers", attachment_type=allure.attachment_type.TEXT)
    
    with allure.step("Отправка GET запроса с заголовками"):
        response = requests.get(url, headers=headers)
    
    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200
    
    with allure.step("Проверка эха заголовка"):
        data = response.json()
        assert data["headers"]["x-custom-header"] == "my-header"


@allure.title("POST /post - urlencoded параметры")
@allure.description("Тест проверяет, что POST /post с urlencoded параметрами попадает в поле form")
@allure.feature("Echo API")
@allure.story("POST /post")
@allure.severity(allure.severity_level.NORMAL)
def test_post_urlencoded_params_in_form():
    """POST /post с urlencoded-параметрами попадает в поле form."""
    url = f"{BASE_URL}/post"
    payload = {"a": "10", "b": "20"}
    
    with allure.step("Подготовка urlencoded данных"):
        allure.attach(str(payload), name="Form Data", attachment_type=allure.attachment_type.TEXT)
    
    with allure.step("Отправка POST запроса с urlencoded"):
        response = requests.post(url, data=payload)
    
    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200
    
    with allure.step("Проверка возвращённых данных"):
        data = response.json()
        assert data["form"]["a"] == "10"
        assert data["form"]["b"] == "20"
