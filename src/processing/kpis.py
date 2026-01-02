import pandas as pd


def generate_kpis(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if "count" not in df.columns:
        df["count"] = 1

    avg_price = df["price"].mean()
    avg_rating = df["rate"].mean()
    inventory_value = (df["price"] * df["count"]).sum()

    return pd.DataFrame(
        {
            "metric": [
                "average_price",
                "average_rating",
                "inventory_value",
            ],
            "value": [
                avg_price,
                avg_rating,
                inventory_value,
            ],
        }
    )

    return kpis
