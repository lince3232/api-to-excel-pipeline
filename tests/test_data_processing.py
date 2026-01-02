import pandas as pd
from processing.data_processing import process_products


def test_process_products_devuelve_dataframe(mocker):
    # Mock de la respuesta de la API
    mock_data = [
        {
            "id": 1,
            "title": "Test product",
            "price": 20.0,
            "rating": {"rate": 4.0}
        }
    ]

    mocker.patch(
        "processing.data_processing.fetch_api_data",
        return_value=mock_data
    )

    # Ejecutamos la función real
    df = process_products("fake_url")

    # Asserts
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert {"id", "title", "price", "rate"}.issubset(df.columns)
