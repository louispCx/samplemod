def get_answer():
    """Get an answer."""
    return True

import requests


def get_btc_usd_value():
    r = requests.get('https://cex.io/api/last_price/BTC/USD')
    r.raise_for_status()
    return r.json()
