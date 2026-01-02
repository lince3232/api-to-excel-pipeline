import requests
import logging

logging.basicConfig(level=logging.INFO)


def fetch_api_data(url: str, params: dict | None = None) -> dict | None:
    """
    Fetch data from an external API.

    Args:
        url (str): API endpoint
        params (dict, optional): Query parameters

    Returns:
        dict | None: JSON response or None if request fails
    """
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        logging.info("API data fetched successfully")
        return response.json()

    except requests.exceptions.Timeout:
        logging.error("Request timeout")

    except requests.exceptions.ConnectionError:
        logging.error("Connection error")

    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP error: {e}")

    except requests.exceptions.RequestException as e:
        logging.error(f"Unexpected request error: {e}")

    return None
