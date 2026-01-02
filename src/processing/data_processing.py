import pandas as pd
from api.api_provider import fetch_api_data


def process_products(api_url: str, params: dict | None = None) -> pd.DataFrame:
    """
    Fetch product data from API and return a cleaned DataFrame.

    Args:
        api_url (str): API endpoint
        params (dict, optional): Query parameters

    Returns:
        pd.DataFrame: Cleaned and sorted product data
    """
    data = fetch_api_data(api_url, params=params)

    if not data:
        return pd.DataFrame()

    df = pd.DataFrame(data)

    # Normalize nested JSON (rating)
    rating_df = pd.json_normalize(df["rating"])
    df = pd.concat([df.drop(columns=["rating"]), rating_df], axis=1)

    # Data cleaning
    df["rate"] = pd.to_numeric(df["rate"], errors="coerce")

    # Sort by rating
    cleaned_df = (
        df.sort_values(by="rate", ascending=False)
          .reset_index(drop=True)
    )

    return cleaned_df
