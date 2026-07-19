import requests

BASE_URL = "https://postman-echo.com"


def test_get_returns_query_params():
    """GET /get должен вернуть квери-параметры в поле args (намеренно сломано)."""
    url = f"{BASE_URL}/get"
    params = {"foo": "bar", "num": "1"}
    response = requests.get(url, params=params)

    assert response.status_code == 200
    data = response.json()
    # здесь специально неверное ожидание
    assert data["args"]["foo"] == "wrong"
    assert data["args"]["num"] == "1"


def test_post_returns_json_body():
    """POST /post c JSON должен вернуть тело в поле json."""
    url = f"{BASE_URL}/post"
    payload = {"name": "Olga", "course": "Python"}
    response = requests.post(url, json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["json"] == payload


def test_post_returns_form_data():
    """POST /post c form-data должен вернуть поля в поле form."""
    url = f"{BASE_URL}/post"
    payload = {"field1": "value1", "field2": "value2"}
    response = requests.post(url, data=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["form"]["field1"] == "value1"
    assert data["form"]["field2"] == "value2"


def test_get_echoes_headers():
    """GET /get должен отразить пользовательский заголовок в headers."""
    url = f"{BASE_URL}/get"
    headers = {"X-Custom-Header": "my-header"}
    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    data = response.json()
    # Postman Echo приводит ключи заголовков к нижнему регистру
    assert data["headers"]["x-custom-header"] == "my-header"


def test_post_urlencoded_params_in_form():
    """POST /post с urlencoded-параметрами попадает в поле form."""
    url = f"{BASE_URL}/post"
    payload = {"a": "10", "b": "20"}
    response = requests.post(url, data=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["form"]["a"] == "10"
    assert data["form"]["b"] == "20"