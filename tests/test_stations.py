from flask.testing import FlaskClient
from http import HTTPStatus

import json


def test_get_all_stations(client: FlaskClient):
    response = client.get("/stations/")

    assert response.status_code == HTTPStatus.OK
    assert response.data is not None

    data = json.loads(response.data.decode("UTF-8").strip())

    assert isinstance(data, dict)
    assert isinstance(data["data"], list)
    assert len(data["data"]) == 1


def test_get_stations_status(client: FlaskClient):
    response = client.get("/stations/bcycle_madison_1874/status")

    assert response.status_code == HTTPStatus.OK
    assert response.data is not None

    response = client.get("/stations/bad_id/status")
    
    assert response.status_code == HTTPStatus.NOT_FOUND
