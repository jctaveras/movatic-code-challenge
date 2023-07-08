CREATE TABLE IF NOT EXISTS movatic.stations (
  station_id STRING NOT NULL,
  lon FLOAT NOT NULL,
  lat FLOAT NOT NULL,
  _bcycle_station_type STRING NOT NULL,
  region_id STRING NOT NULL,
  address STRING NOT NULL,
  name STRING NOT NULL,
  CONSTRAINT "primary" PRIMARY KEY (station_id)
);

CREATE TABLE IF NOT EXISTS movatic.station_status (
  station_id STRING REFERENCES movatic.stations,
  is_returning BOOL NOT NULL,
  is_renting BOOL NOT NULL,
  is_installed BOOL NOT NULL,
  num_docks_available DECIMAL NOT NULL,
  num_bikes_available DECIMAL NOT NULL,
  last_reported TIMESTAMP NOT NULL,
  CONSTRAINT "primary" PRIMARY KEY (station_id)
);


INSERT INTO movatic.stations (
  station_id, lon, lat, _bcycle_station_type, region_id, address, name
) VALUES(
  'bcycle_madison_1874', -89.38527, 43.07571, 'Kiosk and Station', 'bcycle_madison_region_42', '117 Winsconsin Avenue', 'Winsconsin & E. Mifflin'
);

INSERT INTO movatic.station_status (
  station_id, is_returning, is_renting, is_installed, num_docks_available, num_bikes_available, last_reported
) VALUES (
  'bcycle_madison_1874', true, true, true, 7, 2, '2023-07-07T23:37:36.088Z'
);
