from datetime import datetime
from flask import Blueprint, Response, request, jsonify, current_app
from psycopg import Connection
from typing import List

import json
import requests

from movatic.queries import UPSERT_STATION_INFORMATION, UPSERT_STATION_STATUS


ingest_blueprint = Blueprint("ingest", __name__, url_prefix="/ingest")
STATION_INFORMATION_COLUMNS = ['station_id', 'lon', 'lat', '_bcycle_station_type', 'region_id', 'address', 'name']
STATION_STATUS_COLUMNS = ['station_id', 'is_returning', 'is_renting', 'is_installed', 'num_docks_available', 'num_bikes_available', 'last_reported']


@ingest_blueprint.post("/")
def ingest_data() -> Response:
    db: Connection = current_app.config["DB_CONN"]
    url = request.get_json()["url"]
    feeds = requests.get(url).json()["data"]["en"]["feeds"]
    queries = {
        "station_information": UPSERT_STATION_INFORMATION,
        "station_status": UPSERT_STATION_STATUS
    }


    for feed in feeds:
        if feed["name"] in queries.keys():
            stations_data = json.loads(requests.get(feed["url"]).text)["data"]["stations"]
            parameters: List[List[any]] = []

            for data in stations_data:
                match feed["name"]:
                    case "station_information":
                        parameters.append([data.get(key) for key in STATION_INFORMATION_COLUMNS])
                    case "station_status":
                        data["is_returning"] = bool(data["is_returning"])
                        data["is_renting"] = bool(data["is_renting"])
                        data["is_installed"] = bool(data["is_installed"])
                        data["last_reported"] = datetime.utcfromtimestamp(data["last_reported"])
                        parameters.append([data.get(key) for key in STATION_STATUS_COLUMNS])
            
            with db.cursor() as cursor:
                cursor.executemany(queries[feed["name"]], parameters)
                cursor.close()

    return ""
