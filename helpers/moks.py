import requests

from helpers.logger import gen_logger

logger = gen_logger("REST_API")
URL = "http://127.0.0.1:3001/"


def set_mock_config(config):
    logger.info(f"Set config for mock server {config}")
    server_config = {
        "config": config
    }
    response = requests.post(URL + "api/v1/set_config", json=server_config)
    logger.info(f"Response: {response.status_code}, {response.reason}")
    if response.status_code != 200:
        raise ConnectionError(f"{response.status_code}, {response.reason}")


def send_push():
    logger.info("Send push request to Fire Base")
    response = requests.post(URL + "/api/v1/send_push")
    logger.info(response.status_code)
