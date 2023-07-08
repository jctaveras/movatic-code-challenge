# Movatic Backend Code Challenge

Over this repository, you will find a small implementation of three endpoints build on the criteria provide by the Movatic Recruting Team.

## How to execute the project

First of all install all the projects dependencies by running:

```sh
pip3 install -r requirements.txt
```

Now, on your local machine, make sure you have Docker installed, after that you should be able to run the following command:

```sh
docker-compose up -d && flask --app movatic run --debug
```

This will allow the API to run on [your local machine port 5000](http://localhost:5000).

## API

After the server is running on your local machine, you now have access to the followin endpoint:

  - `GET /stations`: is an endpoint that returns all of the available station data inside the database in JSON format.

    ```JSON
    {
      "data": [
        {
          "lon": -89.34747,
          "lat": 43.09423,
          "_bcycle_station_type": "3.0 Dock Station",
          "region_id": "bcycle_madison_region_43",
          "address": "226 Ohio Ave",
          "name": "Ohio Ave @ Capital City Bike Trail",
          "station_id": "bcycle_madison_7370"
        }
        ...
      ]
    }
    ```
  - `GET /stations/{station_id}/status`: an endpoint that will return the most recent status data for a certain the station represented by the `station_id`. This endpoint as well returns the data in JSON fortmat:

    ```JSON
    {
      "data": {
        "is_installed": true,
        "is_renting": true,
        "is_returning": true,
        "last_reported": "Fri, 07 Jul 2023 23:37:36 GMT",
        "num_bikes_available": "2",
        "num_docks_available": "7",
        "station_id": "bcycle_madison_1874"
      }
    }
    ```
  
  - `POST /ingest`: an endpoint that will feed data into the database from a given GBFS URL provided in the request body. This endpoint does not return any data, but a status code based on the outcome of the internal operation

