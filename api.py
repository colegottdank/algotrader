import os

def get_api_key():
    return "AKBHEJ0EK9IO98U9DB8K"


def get_secret_key():
    return "xXdnDTWWyExwkL7jrwsIOiOawnfaUQKVSykMBNk7"


def get_credentials(key_id=None, secret_key=None):
    key_id = key_id or os.environ.get('APCA_API_KEY_ID')
    if key_id is None:
        raise ValueError('Key ID must be given to access Alpaca trade API')

    secret_key = secret_key or os.environ.get('APCA_API_SECRET_KEY')
    if secret_key is None:
        raise ValueError('Secret key must be given to access Alpaca trade API')

    return key_id, secret_key


def get_polygon_credentials(alpaca_key=None):
    try:
        alpaca_key, _ = get_credentials(alpaca_key)
    except ValueError:
        pass
    key_id = os.environ.get('POLYGON_KEY_ID') or alpaca_key
    if key_id is None:
        raise ValueError('Key ID must be given to access Polygon API')
    return key_id