import pandas as pd
from processing.kpis import generate_kpis


def test_generate_kpis_devuelve_dataframe():
    df = pd.DataFrame([
        {"price": 10.0, "rate": 4.5},
        {"price": 20.0, "rate": 3.5},
    ])

    kpis = generate_kpis(df)

    assert isinstance(kpis, pd.DataFrame)
    assert not kpis.empty


def test_generate_kpis_estructura():
    df = pd.DataFrame([
        {"price": 10.0, "rate": 4.5}
    ])

    kpis = generate_kpis(df)

    assert {"metric", "value"}.issubset(kpis.columns)
