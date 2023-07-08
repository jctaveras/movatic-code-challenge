GET_ALL_STATIONS = """
  SELECT * FROM stations;
"""

GET_STATION_STATUS_BY_ID = """
  SELECT * FROM station_status WHERE station_id = %s;
"""

UPSERT_STATION_INFORMATION = """
  UPSERT
    INTO stations (station_id, lon, lat, _bcycle_station_type, region_id, address, name)
    VALUES (%s, %s, %s, %s, %s, %s, %s);
"""

UPSERT_STATION_STATUS = """
  UPSERT
    INTO station_status (station_id, is_returning, is_renting, is_installed, num_docks_available, num_bikes_available, last_reported)
    VALUES (%s, %s, %s, %s, %s, %s, %s);
"""
