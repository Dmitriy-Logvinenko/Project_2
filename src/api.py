import os

from requests import get
from abc import ABC, abstractmethod
from dotenv import load_dotenv

load_dotenv()

opensky_url = os.getenv('OPENSKY_URL')
openstreetmap_url = os.getenv('OPENSTREETMAP_URL')


class BaseAPI(ABC):

    @abstractmethod
    def __init__(self):
        super().__init__()


class APIAdapter(BaseAPI):

    def __init__(self) -> None:
        self.openstreetmap_url = openstreetmap_url
        self.opensky_url = opensky_url
        self.aeroplanes = None

    def get_aeroplanes(self, country: str) -> None:
        headers_nominatim = {
            'User-Agent': 'test-app',
        }

        params_nominatim = {
            'country': country,
            'format': 'json',
            'limit': 1,
        }

        response = get(url=self.openstreetmap_url, params=params_nominatim, headers=headers_nominatim)

        data = response.json()

        geo_coordinates = data[0].get('boundingbox')

        params = {
            'lamin': geo_coordinates[0],
            'lamax': geo_coordinates[1],
            'lomin': geo_coordinates[2],
            'lomax': geo_coordinates[3],
        }

        response = get(url=self.opensky_url, params=params)

        self.aeroplanes = response.json()
