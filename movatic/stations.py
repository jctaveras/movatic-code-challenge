from flask import Blueprint, jsonify, Response, current_app, abort
from psycopg import Connection

from movatic.queries import *


station_blueprint = Blueprint("stations", __name__, url_prefix="/stations")


@station_blueprint.route("/")
def get_all_stations() -> Response:
    db: Connection = current_app.config['DB_CONN']

    with db.cursor() as cursor:
        cursor.execute(GET_ALL_STATIONS)
        data = cursor.fetchall()

        cursor.close()
        
        return jsonify({"data": data})


@station_blueprint.route("/<string:station_id>/status")
def get_station_status(station_id: str) -> Response:
    db: Connection = current_app.config['DB_CONN']

    with db.cursor() as cursor:
        cursor.execute(GET_STATION_STATUS_BY_ID, [station_id])
        data = cursor.fetchone()

        cursor.close()

        if data is None:
            abort(404, description="Station Not Found")
        
        return jsonify({"data": data})    
