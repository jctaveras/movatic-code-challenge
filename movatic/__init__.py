from flask import Flask
from dotenv import load_dotenv

from movatic.stations import station_blueprint
from movatic.ingest import ingest_blueprint
from movatic.db import get_db_connection

import os


def create_app() -> Flask:
    load_dotenv()

    db_url = f"postgres://{os.getenv('COCKROACH_USER')}:{os.getenv('COCKROACH_PASSWORD')}@localhost:26257/{os.getenv('COCKROACH_DATABASE')}"
    app = Flask(__name__)
    app.config.from_mapping(
        DB_CONN = get_db_connection(db_url)
    ) 
    app.register_blueprint(station_blueprint)
    app.register_blueprint(ingest_blueprint)

    return app
