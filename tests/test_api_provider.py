# test/test_api_provider.py
from api.api_provider import fetch_api_data

def test_fetch_api_data_respuesta_valida(mocker):
    mock_response = [
        {"id": 1, "title": "Test product", "price": 10.0, "rating": {"rate": 4.5}}
    ]

    mocker.patch(
        "api.api_provider.requests.get",
        return_value=mocker.Mock(
            status_code=200,
            json=lambda: mock_response,
            raise_for_status=lambda: None
        )
    )

    data = fetch_api_data("https://fakeurl.com")

    assert isinstance(data, list)
    assert len(data) > 0
