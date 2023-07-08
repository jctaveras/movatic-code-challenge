from psycopg import Connection
from psycopg.rows import dict_row

import psycopg


def get_db_connection(db_url: str) -> Connection:
    return psycopg.connect(db_url, application_name="movatic_code_challenge", row_factory=dict_row)
